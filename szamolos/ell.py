global helyes,hibas,megoldas,valasz,ossz
valasz = valasz.get()
if str(valasz) == str(megoldas):
    helyes = int(helyes) + 1
    ossz = int(ossz) + 1
    pontok_kiiras(1, helyes)
elif str(valasz) != str(megoldas):
    hibas = int(hibas) + 1
    ossz = int(ossz) - 1
    pontok_kiiras(2, hibas)
torles()
feladat()