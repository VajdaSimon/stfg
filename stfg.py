#Simple Time Filler Game
import os
import tkinter as tk
from random import randint
from tkinter import *
from functools import partial
import random
import time

window = tk.Tk()
#window.geometry("180x130")

frame = Frame(window)
frame.pack(side="top", expand=True, fill="both")

pontok_spt = "adatok/pontok.spt"
beallitasok_spt = "adatok/beallitasok.spt"

if not os.path.exists("adatok"):
    os.mkdir("adatok")

f = open(pontok_spt, "a+")
f = open(beallitasok_spt, "a+")

if os.stat(pontok_spt).st_size == 0:
    f = open(pontok_spt, "a")
    f.write("0\n0\n0")
    
if os.stat(beallitasok_spt).st_size == 0:
    f = open(beallitasok_spt, "a")
    f.write("-5\n10")

f = open(pontok_spt, "r")
f = f.read()
ossz,helyes,hibas = f.split("\n")

def beallitasok_megnyit():
    f = open(beallitasok_spt, "r")
    f = f.read()
    global szamolos_min,szamolos_max,sorrend_meret,sorrend_max
    szamolos_min,szamolos_max,sorrend_meret,sorrend_max = f.split("\n")

beallitasok_megnyit()

exec(open("szamolos/szamolos.py", "r", encoding='utf8').read())
exec(open("beallitasok/beallitasok.py", "r", encoding='utf8').read())
exec(open("sorrend/sorrend.py", "r", encoding='utf8').read())

def torles():
    for widgets in frame.winfo_children():
        widgets.destroy()

def vissza():
    torles()
    window.geometry("180x150")
    global ossz
    tk.Label(frame, text="Összpont: " + str(ossz)).pack()
    tk.Button(frame, text="Számolós", command=szamolos).pack()
    tk.Button(frame, text="Sorrend", command=sorrend).pack()
    tk.Label(frame, text="").pack()
    tk.Button(frame, text="Beállítások", command=beallitasok).pack()
    tk.Button(frame, text="Kilépés", command=kilepes).pack()
    
def kilepes():
    window.destroy()

vissza()

window.mainloop()