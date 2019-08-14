fami_uid = open("fami_uid.csv", "r")
fami_spot = open("fami_spot.txt", "r")
# data_name = "plan_including_ALL_uniq_location"
data_name = "plan"
plan_data = open(data_name + ".csv", "r")
plan_output = open(data_name + "_fami.csv", "w")
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
                uid_fami_map_companies[key].append(l[x + 2])
            else:
                ls = []
                ls.append(l[x + 2])
                uid_fami_map_companies[key] = ls
    #        print("IN:" + key)
    line = fami_uid.readline().replace("\n", "")

line = plan_data.readline().replace("\n", "")

while line:
    l = line.split(",")
    uid = l[0]
    group = l[1]
    for i in range(2, len(l)):
        location = l[i]
        key = uid + location
        companies_fami = ""
        fami_exclusive = "INVALID"
        if key in uid_fami_map_exclusive:
            fami_exclusive = uid_fami_map_exclusive[key]
        if key in uid_fami_map_companies:
            fami_list = uid_fami_map_companies[key]
            for fami in fami_list:
                companies_fami += fami + ","
            for x in range(len(fami_list), 2):
                companies_fami += "INVALID,"
        else:
            for x in range(0, 2):
                companies_fami += "INVALID,"
        plan_output.write(uid + "," + group + "," + location + "," + fami_exclusive + ","  + companies_fami + "\n")
    line = plan_data.readline().replace("\n", "")
