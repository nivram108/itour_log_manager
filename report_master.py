report_strange_file = open("report_strange.csv", "r")
report_master_output = open("report_master_output.csv", "w")
master_user =  {}
line = report_strange_file.readline()
line = line.replace("\n", "")
while line:
    uid = line.split(",")[1]
    if uid in master_user:
        master_user[uid] += 1
    else:
        master_user[uid] = 1
    line = report_strange_file.readline()
    line = line.replace("\n", "")

for key, value in master_user.items():
    report_master_output.write(key + "," + str(value) + "\n")
