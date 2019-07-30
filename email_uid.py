fi = open("mailuid.txt", "r")
fo = open("mail_uid_map.txt", "w")

line = fi.readline()
while line :
    data = line
    line = fi.readline()
    data = data + "," + line
    data = data.replace("\n", "")
    fo.write(data + "\n")
    line = fi.readline()
