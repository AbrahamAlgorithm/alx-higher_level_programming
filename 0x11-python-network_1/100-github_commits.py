#!/usr/bin/python3
"""Get the 10 latest commit"""

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                      .format(sys.argv[2], sys.argv[1]))
    result = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                  result[i].get("sha"),
                  result[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
