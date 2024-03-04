#!/usr/bin/python3
"""respons value of header with requests"""

if __name__ == "__main__":
    import requests
    import sys

    lis = sys.argv
    r = requests.get(lis[1])
    print(r.headers.get('X-Request-Id'))
