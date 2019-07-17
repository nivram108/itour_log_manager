import json
with open('log_data.json', 'r') as f:
	user_log = json.load(f)

#print(j["-LhzwTYYT-NbfOA6S7xM"]["category"])
for user_key, user_value in user_log.items():
	print(user_key + ":")
	for log_key, log_value in user_value["collections"].items():
		print(" > " + log_value["name"] + ", " + log_value["tag"] + " (" + str(log_value["timestamp"]) + ")")
