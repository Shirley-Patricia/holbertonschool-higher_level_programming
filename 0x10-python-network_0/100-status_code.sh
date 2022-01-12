#!/bin/bash
# sends a request to a URL and displays only the status code of the response, without use pipe, redirection, ; and &&.
curl --write-out '%{http_code}\n' -s --no-keepalive --output /dev/null $1
