#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -s -I -X OPTIONS https://google.com | grep -i allow | awk {'print $2'}
