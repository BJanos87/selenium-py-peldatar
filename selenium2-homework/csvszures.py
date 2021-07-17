import csv

filtered_list = []
with open ("table_in.csv") as csv_file:
    read_file = csv.reader(csv_file, delimiter=',')
    for row in read_file:
        row = row[:2]
        filtered_list.append(row)
    csv_file.close()

with open ("table_in_other.csv", "w") as csv_file:
    write_file = csv.writer(csv_file)
    write_file.writerows(filtered_list)
    csv_file.close()

