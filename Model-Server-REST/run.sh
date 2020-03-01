#!/bin/bash
export GUNICORN_CMD_ARGS="--bind=0.0.0.0"
gunicorn model_server_rest.application.model_endpoint:__hug_wsgi__