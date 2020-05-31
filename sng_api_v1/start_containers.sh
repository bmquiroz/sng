#!/bin/bash

# Get AD secrets
CREDS=`aws --region us-east-1 secretsmanager get-secret-value --secret-id domain.joiner | jq --raw-output '.SecretString' | jq -r '."domain.joiner"'`

docker-compose -f docker-compose.prod.yml up -d --build $CREDS