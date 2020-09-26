# Introduction

An API for the tesla.  Woohoo! The goal is to copy data into grafana for tracking, etc.

## Setup

## Build Script

Run the command `./build.sh` to rebuild the container and update the manifest on our
registry.

## Secrets

Secrets are stored in a kubernetes secret named `credentials` with two kv pairs:

* `SECRET_USERNAME`
* `SECRET_PASSWORD`

## K8s setup

You will need to setup the k8s environment for the pods.  Run the `kubectl apply -k prod` from
the to `k8s` directory create the namespace and to setup the secrets.

## Running manually

Run the command `kubectl delete -k prod` and then `kubectl apply -k prod` to manually run the
command. This should be scheduled to run on Rundeck.

## Scheduled Jobs

This is schedule to run on Rundeck every 15 minutes on k8s1.thesniderpad.com

## Container Updates

This is scheduled for each Saturday night in Rundeck using the `build.sh` script
