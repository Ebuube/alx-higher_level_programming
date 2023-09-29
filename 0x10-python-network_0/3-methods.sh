#!/bin/bash
# show all methods available
curl -ILsX OPTIONS 0.0.0.0:5000/route_4 | grep "Allow: " | cut --delimiter=" " --fields=2-
