#!/bin/bash
# Send a POST request with variables as data
curl -sX POST "$1" --data "email:test@gmail.com&subject=I will always be here for PLD";
