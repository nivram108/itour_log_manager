email_uid_file = open("mail_uid_map.txt", "r")
email_uid_map = {}

line = email_uid_file.readline()
while line:
    line = line.replace("\n", "")
    email_uid_map[(line.split(","))[0]] = line.split(",")[1]
    line = email_uid_file.readline()

email_togo_file = open("mail_togo.csv", "r")

uid_togo_file = open("uid_togo.txt", "w")
line = email_togo_file.readline()
while line:
    line = line.replace("\n", "")
    if line.split(",")[0].lower() in email_uid_map:
        uid_togo_file.write(email_uid_map[line.split(",")[0].lower()] + "," + line.replace(line.split(",")[0] + ",", "") + "\n")
    line = email_togo_file.readline()
