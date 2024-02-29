#!/bin/bash
# Gets the the body length
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
