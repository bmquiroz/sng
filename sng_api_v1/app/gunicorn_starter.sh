#!/bin/sh

/home/sng/sng_api_v1/venv/bin/gunicorn name_string_api:app -b 0.0.0.0:5000