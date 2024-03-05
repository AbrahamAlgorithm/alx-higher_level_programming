#!/usr/bin/python3
"""POST an email using requests"""

if __name__ == "__main__":
    import requests
    import sys

    data = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=data)
    print(r.text)
