char_numb = 97
line = ""

for i in range(26):
    if i > 0 and i % 5 == 0:
        print(line)
        line = ""
    line = line + "\t" + chr(char_numb) + " " + str(char_numb)
    char_numb = char_numb + 1
print(line)
