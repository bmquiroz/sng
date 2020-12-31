#!/bin/bash

# Get AD secrets
# DB_CREDS=`aws --region us-east-1 secretsmanager get-secret-value --secret-id domain.joiner | jq --raw-output '.SecretString' | jq -r '."domain.joiner"'`

SVC_CREDS=sng:A0n0220! docker-compose -f docker-compose.prod.yml up -d --build 

docker-compose -f docker-compose.prod.yml up -d --build 