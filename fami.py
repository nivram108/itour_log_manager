name_uid_file = open("name_uid.csv", "r")
fami_file = open("fami.csv", "r")
fami_uid_output = open("fami_uid.csv", "w")

uid_map = {}
line = name_uid_file.readline()
while line:
    line = line.replace("\n", "")
    l = line.split(",")
    uid_map[l[1]] = l[0]
    line = name_uid_file.readline()

line = fami_file.readline()

while line:
    line = line.replace("\n", "")
    l = line.split(",")
    uid = ""
    if l[0] in uid_map:
        uid = uid_map[l[0]]
    elif l[1] in uid_map:
        uid = uid_map[l[1]]
    else:
        uid = "INVALID"
    fami_uid_output.write(line.replace(l[1], uid))
    line = fami_file.readline()
