#!/bin/bash
# list all allowed methos
curl -sI "$1" | grep "Allow" | cut -d " " -f 2- 
