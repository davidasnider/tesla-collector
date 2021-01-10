# Introduction

![CICD](https://github.com/davidasnider/tesla-collector/workflows/Test%20Build%20Merge%20Deploy/badge.svg)

An API for the Tesla.  Woohoo! The goal is to copy data into grafana for tracking, etc.

## Setup

## GitHub Actions

You can use the local `build.sh` script for testing, but production changes are done
with the `.github` folder workflows. You must do a PR, and if all tests pass it
will be automatically merged.

## Secrets

Secrets are stored in a kubernetes secret named `credentials` with two kv pairs:

- `SECRET_USERNAME`
- `SECRET_PASSWORD`

These are created by ansible, if you are not using my ansible scripts, you must
create this credential manually.

## K8s setup

You will need to setup the k8s environment for the pods. Run the `kubectl apply -k prod` from
the to `k8s` directory create the namespace and to setup the secrets.

## Running manually

Run the command `kubectl delete -k prod` and then `kubectl apply -k prod` to manually run the
command. This should be scheduled to run on Rundeck.

## Scheduled Jobs

This is schedule to run on Rundeck every 15 minutes on k8s1.thesniderpad.com

## Container Updates

This is scheduled for each Saturday night in Rundeck using the `build.sh` script
