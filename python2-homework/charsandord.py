# Deklarálom a szükséges változókat
rm_characters = ["'", '"', '\\n', ',', '_', '?', '.', ':', ';']
text_modded = ""
text_list = []
words_presence = {}

# Beolvasom a TEXT.txt file-t (nyers sorokat listában kapom meg)
with open("TEXT.txt", 'r') as file:
    text = (file.readlines())

# Az így kapott sorok listáján végigiterálok, kitörlöm a nem szükséges karaktereket, illetve kisbetűssé konvertálom
# majd a már formázott sorokat felfűzöm egy nagy string-é
for row in text:
    for character in rm_characters:
        row = row.replace(character, "").lower()
    text_modded = text_modded + row

# A hosszú string-et szétvágom és a benne található szavakat rendezetten egy listába helyezem
text_list = text_modded.split()
text_list.sort()

# Az így kapott szavak listáján végigiterálok, és előfordulás szerint egy szótárba jegyzem be azokat
# {szó : előfurdolás száma}
for word in text_list:
    if not word in words_presence:
        words_presence[word] = 1
    else:
        words_presence[word] += 1

# Az így kapott szótárat string-ként kiírom egy txt fájlba
with open("words_presence.txt", 'w') as new:
    new.write(str(words_presence))
