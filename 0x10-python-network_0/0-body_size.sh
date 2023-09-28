#!/usr/bin/env bash
# Get the size of response in bytes
curl -s --write-out "%{size_download}" -o /dev/null localhost | cut --fields=4 --delimiter=' '
