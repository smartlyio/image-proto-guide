import json
import requests
import time

analyze_headers = {}

# Get access token which lasts only up to 72 hours at a time
def connect(client_id, client_secret):
  global analyze_headers

  token_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
  secrets = {
      'clientId': client_id,
      'clientSecret': client_secret
  }
  r = requests.post('https://vision-api.eyeem.com/v1/token', headers=token_headers, data=secrets)
  token_data = r.json()
  analyze_headers = {
      'Authorization': str(token_data['token_type'] + ' ' + token_data['access_token']),
      'Content-Type': 'application/json'
  }
  print("EyeEm Api token updated")

# Classify images
custom_endpoints = {
}

def fetch_analysis(data):
    r = requests.post('https://vision-api.eyeem.com/v1/analyze', headers=analyze_headers, data=json.dumps(data))
    results = r.json()
    print(results)
    # time.sleep(2)  # max 30 images per minute
    return results

def fetch_custom_endpoints(image_url):
    scores = {}
    for model_name, model_id in custom_endpoints.items():
        analyze_data = {
            'requests': [{
                'tasks': [{
                    'type': 'PERSONALIZED_SCORE',
                    'modelId': model_id
                }],
                'image': {'url': image_url}
            }]
        }
        results = fetch_analysis(analyze_data)
        model_score = results['responses'][0]['personalized_scores']['scores'][model_id]
        scores[model_name] = model_score
    return scores


# Tasks
TAGS = 'TAGS'
CAPTIONS = 'CAPTIONS'
AESTHETIC = 'AESTHETIC_SCORE'
CUSTOM_ENDPOINTS = 'CUSTOM_ENDPOINTS'

def score_image_file(filename, tasks=[TAGS, AESTHETIC]):
  encoded_string = r''
  with open(filename, "rb") as image_file:
      encoded_string = base64.standard_b64encode(image_file.read()).decode('utf8')
  
  image = {'content': encoded_string}
  return eyeem.score_image(encoded_string)

def score_image_url(image_url, tasks=[TAGS, AESTHETIC]):
  return score_image({'url': image_url}, tasks)

def score_image(image, tasks):
    analysis_tasks = [{
      "type": task
    } for task in tasks if task in [TAGS, CAPTIONS, AESTHETIC]]

    # aesthetic
    analyze_data = {
        'requests': [{
            'tasks': analysis_tasks,
            'image': image
        }]
    }

    results = fetch_analysis(analyze_data)
    scores = {}
    first_result = results['responses'][0]
    if ('aesthetic_score' in first_result):
      scores['aesthetic'] = first_result['aesthetic_score']['score']
    if ('tags' in first_result):
      scores['tags'] = json.dumps(first_result['tags'])
    if ('captions' in first_result):
      scores['captions'] = json.dumps(first_result['captions'])

    # Personalized scores within custom endpoints cannot be fetched with the same request
    if CUSTOM_ENDPOINTS in tasks:
        scores.update(fetch_custom_endpoints(image_url))

    return scores