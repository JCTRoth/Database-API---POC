#!/usr/bin/bash
gunicorn3 --reload restApi:api #Do not use Reload for Prod.