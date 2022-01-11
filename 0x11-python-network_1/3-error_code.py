#!/usr/bin/python3
# Write a Python script that fetches https://intranet.hbtn.io/status

from urllib import request
import urllib.Error
import sys

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
