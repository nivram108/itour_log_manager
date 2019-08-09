fami_uid = open("fami_uid.csv", "r")
fami_spot = open("fami_spot.txt", "r")
viewed_checkin = open("viewed_community.csv", "r")
view_inclusive = open("view_inclusive.csv", "w")
view_exclusive = open("view_exclusive.csv", "w")
spots = fami_spot.readline().replace("\n", "").split(",")
uid_fami_map_companies = {}
uid_fami_map_exclusive = {}
fami_value_map = {}
fami_value_map["去過"] = 3
fami_value_map["不確定"] = 2
fami_value_map["沒去過"] = 1

line = fami_uid.readline().replace("\n", "")
while line:
    l = line.split(",")
    uid = l[1]
    if uid == "INVALID":
        line = line
    elif not "_" in uid:
        for x in range(len(spots)):
            key = uid + spots[x]
            uid_fami_map_exclusive[key] = l[x + 2]
     #       print("EX:" + key)
    else:
        for x in range(len(spots)):
            uid = uid.replace("_", "")
            key = uid + spots[x]
            if key in uid_fami_map_companies :
                uid_fami_map_companies[key].add(l[x + 2])
            else:
                ls = []
                ls.add(l[x + 2])
                uid_fami_map_companies[key] = ls
    #        print("IN:" + key)
    line = fami_uid.readline().replace("\n", "")

line = viewed_checkin.readline().replace("\n", "")
while line:
    l = line.split(",")
    key = l[0] + l[2]
    fami_inclusive = "INVALID"
   # print("find key:" + key)
    if key in uid_fami_map_exclusive:
        fami_exclusive = uid_fami_map_exclusive[key]
    is_poi = l[2] in spots
    companies_fami = ""
    for key, fami_list in uid_fami_map_companies.items():
        for fami in fami_list:
            companies_fami += fami + ","
        for x in range(len(fami_list), 4):
            companies_fami += "INVALID,"
    view_exclusive.write(line + "," + fami_exclusive + "," + str(is_poi) + "\n")
    view_inclusive.write(line + "," + fami_exclusive + ","  + companies_fami + str(is_poi) + "\n")
    line = viewed_checkin.readline().replace("\n", "")
