import requests
import json

SELECT_URL = 'http://localhost:8983/solr/news/select'

# Find articles related to homicides investigated by the FBI in 2017

params = {
    'defType': 'edismax',
    'q': 'homicides FBI',
    'indent': 'true',
    'q.op': 'AND',
    'qf': 'title content',
    'fq': 'date:[2017-01-01T00:00:00Z TO 2017-12-31T23:59:59Z]',
    'bq': 'title:homicides^2.0 content:homicides^2.0'
}


response = requests.get(SELECT_URL, params=params)

result_json = response.json()

print(json.dumps(result_json, indent=2))