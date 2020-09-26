#!/usr/bin/env bash -l
set -Eeuo
export DOCKER_CLI_EXPERIMENTAL=enabled

IMAGE="registry.thesniderpad.com/tesla"

docker buildx build --no-cache --platform linux/arm/v7,linux/amd64 --tag $IMAGE --push .
