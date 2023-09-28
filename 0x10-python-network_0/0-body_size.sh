#!/bin/bash
# Get the size of response in bytes
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f 2
