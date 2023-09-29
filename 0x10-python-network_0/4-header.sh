#!/bin/bash
# Send a GET request with a header variable
curl --silent --request GET --header "X-SChoool-User-Id:98" "$1";
