#!/bin/bash
# Send a JSON file using POST HTTP/1.0 method in curl command
curl -X POST -L -H 'Content-Type: application/json' -d @"$2" "$1"
