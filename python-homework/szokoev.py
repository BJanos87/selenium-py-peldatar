def szokoev(evszam):
    if int(evszam) % 4 == 0:
        if int(evszam) % 100 == 0:
            if int(evszam) % 400 == 0:
                print(evszam,"Szökőév")
            else:
                print(evszam,"Nem szökőév")
        else:
            print(evszam,"Szökőév")
    else:
        print(evszam,"Nem szökőév")

year = input("Kérlek adj meg egy évszámot: ")
szokoev(year)
