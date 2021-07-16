with open("adat.txt", "r") as file:
    rows = file.readlines()
    file.close()
with open("fajl3_other.txt", "w") as file_other:
    file_other.write(str(rows))
    file_other.close()
