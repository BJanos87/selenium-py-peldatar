with open("adat.txt", "r") as file:
    rows = file.readlines()
    file.close()
with open("fajl4_other.txt", "w") as file_other:
    for row in rows:
        file_other.write(row)
    file_other.close()
