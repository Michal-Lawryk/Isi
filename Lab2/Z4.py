import csv

with open('pc.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["pc_name", "ip"]
    ip = "172.30.2."
    writer.writerow(field)
    for x in range(1, 101):
        writer.writerow(["P" + str(x), ip + str(x)])
