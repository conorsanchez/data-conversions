#read superhero json
import json
from pprint import pprint

with open('superheroes.json', 'w') as f:
	data = json.load(f)

all_powers = []

#get members
members = data['members']
#loops over the members
for m in members
	powers = m['powers']
		for p in powers:
		all_powers.append(p)

# for each member, et their powers


#print list to terminal
unique_powers = list(set(powers))
print all_powers