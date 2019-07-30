id_file = open("email_id.txt", "r")
uid_file = open("mail_uid_map.txt", "r")
uid_id_map = open("uid_id_map.txt", "w")

uid_map = {}
line = uid_file.readline()
while line:
    line = line.replace("\n", "")
    l = line.split(",")
    uid_map[l[0].lower()] = l[1]
    line = uid_file.readline()

line = id_file.readline()

while line:
    line = line.replace("\n", "")
    l = line.split(",")
    if l[0].lower() in uid_map:
        uid_id_map.write(uid_map[l[0].lower()] + "," + l[1] + "\n")
    line = id_file.readline()
