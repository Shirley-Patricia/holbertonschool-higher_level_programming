#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -i $1 | grep -i HTTP/ | awk '{if ($2 == 200) print "Route 2"}'
