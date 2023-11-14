import requests
import json

SELECT_URL = 'http://localhost:8983/solr/news/select'

# Find news about LeBron's good performances in lost games

params = {
    'defType': 'edismax',
    'q': 'LeBron good performance lost game points',
    'indent': 'true',
    'q.op': 'AND',
    'qf': 'title^1.5 content',
    "fl":"id, title, author, date, publisher, category, content, score",
    'bq': 'title:Lebron^3 title:lost^1.5 title:game^1.5 content:Lebron^2.5 content:lost^2 content:game^1.5'
}


response = requests.get(SELECT_URL, params=params)

result_json = response.json()

print(json.dumps(result_json, indent=2))