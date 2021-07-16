with open("adat.txt", "r") as file:
    with open("fajl5_other.txt", "w") as file_other:
        for rows in file:
            for word in rows:
                file_other.write(word)
        file.close()
        file_other.close()
