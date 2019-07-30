report_strange_file = open("report_strange.csv", "r")
report_strange_output = open("report_strange_output.csv", "w")
line = report_strange_file.readline()
line = line.replace("\n", "")
while line:
    print(line.split(",")[-1])
    if int(line.split(",")[-1]) <= 0 :
        line = line.replace(line.split(",")[-1], "")
    elif int(line.split(",")[-1]) <= 60:
        line = line + ",LESS THAN ONE MINUTE"
    report_strange_output.write(line + "\n")
    line = report_strange_file.readline()
    line = line.replace("\n", "")
