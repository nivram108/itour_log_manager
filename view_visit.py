report_file = open("report_log.csv", "r")
view_file = open("view_log.csv", "r")
view_visit_file = open("view_visit.csv", "w")

line = report_file.readline().replace("\n", "") #head
line = report_file.readline().replace("\n", "")
report_user_timestamp_map = {}
while line:
    l = line.split(",")
    user = l[1]
    location = l[4]
    timestamp = int(l[-1])
    key = user + location
    if location != "":
        if key in report_user_timestamp_map:
            if timestamp > report_user_timestamp_map[key]:
                report_user_timestamp_map[key] = timestamp
        else:
            report_user_timestamp_map[key] = timestamp
    line = report_file.readline().replace("\n", "")

line = view_file.readline().replace("\n", "")#head
line = view_file.readline().replace("\n", "")
while line:
    l = line.split(",")
    user = l[0]
    location = l[2]
    timestamp = int(l[-1])
    key = user + location
    isvisit = "FALSE"
    if (key in report_user_timestamp_map) and (report_user_timestamp_map[key] > timestamp):
        isvisit = "TRUE"
    view_visit_file.write(line + "," + isvisit + "\n")
    line = view_file.readline().replace("\n", "")
