number = input("Kérlek adj meg egy számot: ")
number_list = []
reversed_list = []
counter = -1

while int(number) > 0:
    number_list.append(number)
    number = input("Kérlek adj meg még egy számot: ")

for i in range(len(number_list)):
    reversed_list.append(number_list[counter])
    counter = counter - 1

print(reversed_list)

