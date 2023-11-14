import requests
import json

SELECT_URL = 'http://localhost:8983/solr/news/select'

# Find news articles where Trump spoke on the immigration crisis

params = {
    'defType': 'edismax',
    'q': 'Trump immigration crisis',
    'indent': 'true',
    'q.op': 'AND',
    'qf': 'title^2.5 content',
    "fl":"id, title, author, date, publisher, category, content, score",
    'bq': 'title:Trump^2.5 title:immigration^1.5 content:Trump^2.5 content:immigration^1.5'
}

response = requests.get(SELECT_URL, params=params)

result_json = response.json()

print(json.dumps(result_json, indent=2))