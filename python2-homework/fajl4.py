with open("adat.txt", "r") as file:
    rows = file.readlines()
    file.close()
with open("fajl4_other.txt", "w") as file_other:
    for word in rows:
        file_other.write(word)
    file_other.close()
