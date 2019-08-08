from User import *
from time import gmtime, strftime
import json
import collections

#version = "community"
version = "google"
output_file_name = version + ".csv"
# output_file_name = "output_" + strftime("%m%d_%H_%M_%S", gmtime()) + ".csv"
checkin_location_dict = {}
reported_file = open("reported_" + output_file_name, "a")
unvisited_file = open("unvisited_" + output_file_name, "a")

def main():
    reported_file.write("uid,name,location,togo,notification hot checkin,news hot checkin,notification hot spot,news hot spot,viewed checkin,liked,saved,type,timestamp\n")
    reported_file.close()
    unvisited_file.write("uid,name,location,togo,notification hot checkin,news hot checkin,notification hot spot,news hot spot,viewed checkin,liked,saved\n")
    unvisited_file.close()
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
    global output_file_name
    global version
    user = User("", "", checkin_location_dict, "")
    # with open('log_cummunity.json', 'r') as f:
    with open("log_" + version + ".json", 'r') as f:
        user_log = json.load(f)
    for user_key, user_value in user_log.items():
        for log_key, log_value in user_value["collections"].items():
            if not user.uid == log_value["uid"]:
                new_user = User(log_value["uid"], log_value["name"], checkin_location_dict, output_file_name)
                user = new_user
            user.read_log(log_value["tag"], log_value["msg"], log_value["timestamp"])
        user.write_data()
main()
