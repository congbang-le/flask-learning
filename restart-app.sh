#!/usr/bin/bash

docker build -t flask-playground:latest .
docker run -p 8000:80 flask-playground:latest