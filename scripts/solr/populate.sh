#!/bin/bash

# Populate the news collection
curl -X POST -H 'Content-type: application/json' \
    --data-binary "@./../../solr/news.json" \
    http://localhost:8983/solr/news/update?commit=true
