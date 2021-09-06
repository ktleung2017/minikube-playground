#!/usr/bin/env bash
set -ex

docker build -t seldon-app:latest -f Dockerfile_seldon .
