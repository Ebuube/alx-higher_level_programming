#!/bin/bash
# Send a POST request with variables as data
curl -sX POST --data "email:test@gmail.com&subject=I will always be here for PLD" "$1";
