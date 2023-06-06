#!/bin/bash

CURRENT_PID=$(lsof -i :8000 -t)
echo "> CURRENT_PID: $CURRENT_PID"

if [ -z "$CURRENT_PID" ]; then
  ehco "> Not currently running"
else
  echo "> kill -9 $CURRENT_PID"
  kill -9 "$CURRENT_PID"
  sleep 2
fi

echo "> pip3 install -r ./practice-django/requirements.txt"
pip3 install -r ./requirements.txt
sleep 2

echo "> run server"
nohup python3 ./manage.py runserver 0.0.0.0:8000 >/dev/null 2>&1 &