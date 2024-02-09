#!/usr/bin/python3
"""
This script reads a JSON file, loads its contents into a Python list, and
appends the command line arguments to that list. The updated list is then
saved back to the JSON file.

Usage:
    ./script_name.py arg1 arg2 arg3 ...

    Args:
        arg1, arg2, arg3, ... : Command line arguments to be added to the list.

Note:
    If the specified JSON file does not exist or cannot be decoded, an empty
    list is created.

Example:
    ./script_name.py item1 item2 item3
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = 'add_item.json'
with open(filename, mode='r+', encoding='UTF-8') as json_file:
    json_string = json_file.read()
    try:
        obj = json.loads(json_string)
    except json.decoder.JSONDecodeError:
        obj = []

    obj.extend(sys.argv[1:])  # store command line arguments in the list
    save_to_json_file(obj, filename)
