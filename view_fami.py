fami_uid = open("fami_uid.csv", "r")
fami_spot = open("fami_spot.txt", "r")
viewed_checkin = open("viewed_community.csv", "r")
view_inclusive = open("view_inclusive.csv", "w")
view_exclusive = open("view_exclusive.csv", "w")
spots = fami_spot.readline().replace("\n", "").split(",")
uid_fami_map_inclusive = {}
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
            uid_fami_map_inclusive[key] = l[x + 2]
            print("EX:" + key)
    else:
        for x in range(len(spots)):
            key = uid + spots[x]
            if key in uid_fami_map_inclusive :
                if uid_fami_map_inclusive[key] < l[x + 2]:
                    uid_fami_map_inclusive[key] = l[x + 2]
            else:
                uid_fami_map_inclusive[key] = l[x + 2]
            print("IN:" + key)
    line = fami_uid.readline().replace("\n", "")

line = viewed_checkin.readline().replace("\n", "")
while line:
    l = line.split(",")
    key = l[0] + l[2]
    fami_exclusive = "INVALID"
    fami_inclusive = "INVALID"
    print("find key:" + key)
    if key in uid_fami_map_exclusive:
        fami_exclusive = uid_fami_map_exclusive[key]
    if key in uid_fami_map_inclusive:
        fami_inclusive = uid_fami_map_inclusive[key]
    is_poi = l[2] in spots
    view_exclusive.write(line + "," + fami_exclusive + "," + is_poi + "\n")
    view_inclusive.write(line + "," + fami_inclusive + "," + is_poi + "\n")
    line = viewed_checkin.readline().replace("\n", "")
