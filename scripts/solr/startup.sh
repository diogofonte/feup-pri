#!/bin/bash

# This script expects a container started with the following command.
docker run -p 8983:8983 --name news_solr -d solr:9.3 solr-precreate news