#!/bin/bash
# Get the size of response in bytes
curl -s -o /dev/null -w "%{size_download}\n" localhost
