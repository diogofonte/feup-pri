import requests
import json

SELECT_URL = 'http://localhost:8983/solr/news/select'

# Find news about LeBron's good performances in lost games

params = {
    'defType': 'edismax',
    'q': 'LeBron good performance "lost games"',
    'indent': 'true',
    'q.op': 'AND',
    'qf': 'title^2 content'
}


response = requests.get(SELECT_URL, params=params)

result_json = response.json()

print(json.dumps(result_json, indent=2))