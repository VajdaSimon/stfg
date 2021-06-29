#Simple Time Filler Game
import os
from random import randint

f = open("adatok.spt", "a+")

if os.stat('adatok.spt').st_size == 0:
    f = open("adatok.spt", "a")
    f.write("0\n0")

def pontok():
    f = open("adatok.spt", "r")
    f = f.read()
    global helyes,hibas
    helyes,hibas = f.split("\n")
    print("Eddig helyesen megoldva: " + helyes)
    print("Eddig hibássan megoldva: " + hibas)
    plus()

def plus():
    global helyes,hibas
    helyes = int(helyes)
    hibas = int(hibas)
    sze = randint(-5, 10)
    szm = randint(-5, 10)
    megoldas = sze + szm
    valasz = input(str(sze) + "+" + str(szm) + "=")
    if str(valasz) == "p":
        pontok()
    elif str(valasz) == str(megoldas):
        helyes += 1
        open("adatok.spt", "w+").write(str(helyes) + "\n" + str(hibas))
    elif str(valasz) != str(megoldas):
        hibas += 1
        open("adatok.spt", "w+").write(str(helyes) + "\n" + str(hibas))
    plus()
    
pontok()