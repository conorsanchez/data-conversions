vegetables = [
 {'name': 'eggplant'},
 {'name': 'tomato'},
 {'name': 'corn'},
 {'name': 'bellpepper'}
]

#write header file to csv
import csv

with open('testwrite.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'length'])

	#loop through each vegetable
	for veggie in vegetables:
	#for each vef write a row to the csv
		name = veggie['name']
		length = len(name)
		writer.writerow([name, length])