#!/usr/bin/python3
"""handling error code wih urllib request"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as request:
            print(request.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
