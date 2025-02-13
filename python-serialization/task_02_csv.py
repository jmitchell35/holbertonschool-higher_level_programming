#!/usr/bin/env python3
import csv 
import json

def convert_csv_to_json(csv_source):
    try:
        csv_data = open(csv_source, newline='')
        rows_list = list(csv.DictReader(csv_data))
        print(rows_list)
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(rows_list, file, indent=4)
        csv_data.close()
        return True
    except Exception as e:
        print(f"{e}")
        return False