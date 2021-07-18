with open("adat.txt", "r") as file:
    with open("fajl5_other.txt", "w") as file_other:
        for rows in file:
            file_other.write(rows)
        file.close()
        file_other.close()
