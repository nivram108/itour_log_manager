report_strange_file = open("report_strange_output.csv", "r")
report_master_output = open("report_master_output.csv", "w")
report_master_input = open("report_master_output.csv", "r")
master_user =  {}
user_group = {}
uid_index = 1
report_type_index = 13
line = report_strange_file.readline()
line = line.replace("\n", "")
while line:
    user_group[line.split(",")[1]] = line.split(",")[2]
    uid = line.split(",")[1] + "," + line.split(",")[13]
    if uid in master_user:
        master_user[uid] += 1
    else:
        master_user[uid] = 1
    line = report_strange_file.readline()
    line = line.replace("\n", "")

for i in range(81):
    uid = "U" + str(i + 1)
    if i + 1 < 10 :
        uid = "U0" + str(i + 1)
    group = "INVALID"
    if uid in user_group:
        group = user_group[uid]
    line = uid + "," + group + ","
    num = 0
    key = uid + "," + "add check"
    if key in master_user:
        num = master_user[key]
    line += str(num) + ","
    num = 0
    key = uid + "," + "report anywhere"
    if key in master_user:
        num = master_user[key]
    line += str(num) + ","
    num = 0
    key = uid + "," + "report togo"
    if key in master_user:
        num = master_user[key]
    line += str(num) + "\n"
    report_master_output.write(line)
