#!/usr/bin/python3
"""add all argumenst to a json file"""


if __name__ == "__main__":
    import sys

    loader = __import__('6-load_from_json_file').load_from_json_file
    saver = __import__('5-save_to_json_file').save_to_json_file
    try:
        items = loader('add_item.json')
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    saver(items, 'add_item.json')
