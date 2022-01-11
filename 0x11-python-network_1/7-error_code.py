#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter,
   and displays the body of the response (decoded in utf-8) using requests
"""

if __name__ == "__main__":
    import requests
    import sys

    req = requests.get(sys.argv[1])
    if req.raise_for_status():
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
