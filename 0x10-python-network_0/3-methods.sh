#!/bin/bash
# show all methods available
curl -ILsX OPTIONS "$1" | grep "Allow: " | cut --delimiter=" " --fields=2-
