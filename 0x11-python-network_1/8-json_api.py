#!/usr/bin/python3
"""get json element"""

if __name__ == "__main__":
    import requests
    import sys

    data = {}
    data['q'] = '' if (len(sys.argv) == 1) else sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        c = r.json()
        if (c == {}):
            print('No result')
        else:
            print('[{}] {}'.format(c['id'], c['name']))
    except ValueError:
        print('Not a valid JSON')
