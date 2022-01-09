#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -I $URL | grep -i Content-Length | awk '{print $2}'
