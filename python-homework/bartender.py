age = input("Hány éves vagy?: ")
ital = input("Milyen itallal szolgálhatok?: ")

if int(age) < 18:
    if ital == "sör":
        print("Sajnos kiskorúakat nem áll módunkban alkohollal kiszolgálni, kólát tudunk helyette ajánlani")
    elif ital == "kóla":
        print("Parancsolj a kólád, fogyaszd egészséggel")
    else:
        print("Csokoládé elfogyott, pisztácia nem is volt... Kólát tudok esetleg ajánlani")
elif int(age) > 60:
    if ital == "kóla":
        print("Sajnálattal közlöm, hogy a koffein megemeli a vérnyomását, így az ön érdekében nem áll módomban kiszolgálni önt")
    elif ital == "sör":
        print("Parancsoljon a söre, fogyassza egészséggel")
    else:
        print("Csokoládé elfogyott, pisztácia nem is volt... Sört tudok esetleg ajánlani")
else:
    if ital == "sör":
        print("Parancsoljon a söre, fogyassza egészséggel")
    elif ital == "kóla":
        print("Parancsoljon a kólája, fogyassza egészséggel")
    else:
        print("Csokoládé elfogyott, pisztácia nem is volt... Sört vagy kólát tudok esetleg ajánlani")

