#!/bin/bash
# push json
curl -s -X POST -H 'Content-Type: application/json' -d @"$2" "$1"
