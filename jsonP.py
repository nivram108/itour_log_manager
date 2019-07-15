import json
with open('itour-3a659-before_pilot-export.json', 'r') as f:
	j = json.load(f)

print(j["-LhzwTYYT-NbfOA6S7xM"]["category"])
#for key, value in j.items():
#	print(key + ", " + value["location"])