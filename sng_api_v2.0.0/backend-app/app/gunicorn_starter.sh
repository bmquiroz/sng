#!/bin/sh

/home/sng/sng_api/venv/bin/gunicorn \
--timeout 60 \
--log-level=DEBUG \
--workers=2 \
name_string_api:app -b 0.0.0.0:5000
