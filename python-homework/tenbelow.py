number = input("Kérem adjon meg egy számot: ")
result = 0
given_numbers = ""

while int(number) < 10:
    result = int(number) + result
    given_numbers = given_numbers + " " + number
    number = input("Kérem adjon meg még további számot: ")
    if int(number) > 10:
        break

print("A megadott számok sorozata:",given_numbers.strip())
print("A megadott számok összege:",result)