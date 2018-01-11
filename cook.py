import csv

with open('veggies.csv') as f:
	reader = csv.DictReader(f)
	vegetables = list(reader), 

import json

with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent=2)