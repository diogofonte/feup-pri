#!/bin/bash

# Description: Script to create the schema for the news collection
docker cp ./../../solr/mapping_accents.txt news_solr:/var/solr/data/news/conf/mapping_accents.txt
docker cp ./../../solr/synonyms.txt news_solr:/var/solr/data/news/conf/synonyms.txt

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary "@./../../solr/schema.json" \
    http://localhost:8983/solr/news/schema