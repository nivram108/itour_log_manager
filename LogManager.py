from User import *
from time import gmtime, strftime
import json
import collections

output_file_name = "output_" + strftime("%m%d_%H_%M_%S", gmtime()) + ".txt"
checkin_location_dict = {}

def main():
    set_checkin_location_dict()
    read_log()
def set_checkin_location_dict():
    global checkin_location_dict
    with open('checkin_data.json', 'r') as f:
    	checkin_data = json.load(f)
    for key, value in checkin_data.items():
        checkin_location_dict[key] = value["location"]
def read_log():
    global checkin_location_dict
    user = User("", "", checkin_location_dict)
    with open('log_data.json', 'r') as f:
    	user_log = json.load(f)
    for user_key, user_value in user_log.items():
    	for log_key, log_value in user_value["collections"].items():
            if not user.uid == log_value["uid"]:
                new_user = User(log_value["uid"], log_value["name"], checkin_location_dict)
                user = new_user
                #print(user.uid + " is " + user.name)
            #user.read_log(log_value["tag"], log_value["msg"], log_value["msg"], log_value["timestamp"])
            user.read_log(0, 0, 0, 0)

    		#print(" > " + log_value["name"] + ", " + log_value["tag"] + " (" + str(log_value["timestamp"]) + ")")
main()
