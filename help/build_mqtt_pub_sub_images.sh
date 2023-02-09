#!/bin/sh

# Build pub-sub MQTT images that described on Dockerfile_publish & Dockerfile_subscribe
docker build --tag mqtt_pub:v1 --file Dockerfile_pub .
docker build --tag mqtt_sub:v1 --file Dockerfile_sub .
