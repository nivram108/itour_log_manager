from LogToSort import *
community_file = open("reported_community.csv", "r")
google_file = open("reported_google.csv", "r")
report_file = open("reported_summary.csv", "w")
additional_info = open("additional_info.csv", "w")

line = community_file.readline()
line = line.replace("\n", "")
user_data = []
uid = line.split(",")[0]
while line:
    user_data.append(LogToSort())


    line = community_file.readline()
    line = line.replace("\n", "")
    uid = line.split(",")[0]
