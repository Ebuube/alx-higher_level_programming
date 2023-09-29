#!/bin/bash
# Send a GET request with a header variable
curl -sX GET --header "X-School-User-Id:98" "$1";
