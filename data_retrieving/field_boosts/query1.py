import requests
import json

SELECT_URL = 'http://localhost:8983/solr/news/select'

# Find news articles where Trump spoke on the immigration crisis

params = {
    'defType': 'edismax',
    'q': 'Trump immigration crisis',
    'indent': 'true',
    'q.op': 'AND',
    'qf': 'title content'
}

response = requests.get(SELECT_URL, params=params)

result_json = response.json()

print(json.dumps(result_json, indent=2))