log_file = open("report_summary.csv", "r")
spot_file = open("spot.txt", "r")

report_including_ONLYPOI = open("report_including_ONLYPOI.csv", "w")
report_including_ALL = open("report_including_ALL.csv", "w")

user_visited_location = {}
spot_map = {}
uid = ""

line = spot_file.readline()
while line:
    line = line.replace("\n", "")
    spot_map[line] = True
    line = spot_file.readline()
line = log_file.readline()
line = log_file.readline()
while line:
    line = line.replace("\n", "")
    print("uid:" + line.split(",")[1])
    if uid != line.split(",")[1]:
        uid = line.split(",")[1]
        user_visited_location.clear()
    location = line.split(",")[4]
    if location == "":
        report_including_ALL.write(line + "\n")
    elif (location in user_visited_location) == False:
        user_visited_location[location] = True
        print(str(uid) + ", " + location)
        report_including_ALL.write(line + "\n")
        if location in spot_map:
            report_including_ONLYPOI.write(line + "\n")
    line = log_file.readline()
