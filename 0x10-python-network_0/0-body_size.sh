#!/usr/bin/env bash
# Get the size of response in bytes
curl -s "$1" | wc -c
