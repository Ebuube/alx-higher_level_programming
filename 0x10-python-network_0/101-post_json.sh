#!/bin/bash
# Send a JSON file using POST HTTP/1.0 method in curl command
curl -X POST -H "Content-Type: application/json" @"$2" "$1"
