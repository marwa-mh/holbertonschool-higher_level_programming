#!/usr/bin/python3
""" creates an Object from a “JSON file” """
import json
import sys
from os import path
save_to_json_file =__import__('5-save_to_json_file').save_to_json_file
load_from_json_file =__import__('6-load_from_json_file').load_from_json_file
data:list
filename ='add_item.json'

if path.exists(filename):
    try:
        data = load_from_json_file(filename)
    except:
        data = []
else:
    data = []

data.extend(sys.argv[1:])

save_to_json_file(data, filename)
