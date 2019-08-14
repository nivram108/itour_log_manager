fami_uid = open("fami_uid.csv", "r")
fami_spot = open("fami_spot.txt", "r")
# data_name = "report_including_ALL_uniq_location"
data_name = "report_including_ONLYPOI_uniq_location"
report_data = open(data_name + ".csv", "r")
report_output = open(data_name + "_fami.csv", "w")
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

line = report_data.readline().replace("\n", "")
while line:
    l = line.split(",")
    key = l[1] + l[4]
    fami_exclusive = "INVALID"
   # print("find key:" + key)
    if key in uid_fami_map_exclusive:
        fami_exclusive = uid_fami_map_exclusive[key]
    is_poi = l[2] in spots
    companies_fami = ""
    if key in uid_fami_map_companies:
        fami_list = uid_fami_map_companies[key]
        for fami in fami_list:
            companies_fami += fami + ","
        for x in range(len(fami_list), 4):
            companies_fami += "INVALID,"
    else:
        for x in range(0, 4):
            companies_fami += "INVALID,"
    report_output.write(line + "," + fami_exclusive + ","  + companies_fami + str(is_poi) + "\n")
    line = report_data.readline().replace("\n", "")
