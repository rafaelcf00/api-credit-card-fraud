import csv
import json

def convert_to_json(file):
    if file:
        with open(file, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)    
            data = [row for row in csv_reader]
            json_data = json.dumps(data)

        return json_data