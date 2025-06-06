#!/usr/bin/python3
"""reading data from one format (CSV)
 and converting it into another
 format (JSON) using serialization techniques."""
import csv
import json


def convert_csv_to_json(filename: str):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))

        with open("data.json", "w", encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile)
    except Exception as e:
        return False
    return True
