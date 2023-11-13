import requests
import json

SELECT_URL = 'http://localhost:8983/solr/news/select'

# Find news articles regarding the conflicts between republicans and democrats about gun ownership

params = {
    'defType': 'edismax',
    'q': 'Republicans Democrats "gun ownership" conflicts',
    'indent': 'true',
    'q.op': 'AND',
    'qf': 'title content',
    'bq': 'title:gun^2.5 title:conflits^1.5 content:gun^2.5 content:conflits^1.5'
}


response = requests.get(SELECT_URL, params=params)

result_json = response.json()

print(json.dumps(result_json, indent=2))