#Simple Time Filler Game
import os
import tkinter as tk
from random import randint
from tkinter import *
from functools import partial
import random
import time

window = tk.Tk()
window.resizable(False,False)

frame = Frame(window)
frame.pack(side="top", expand=True, fill="both")

exec(open("adatok/betoltes.py", "r", encoding='utf8').read())
exec(open("adatok/kiiras.py", "r", encoding='utf8').read())
exec(open("szamolos/szamolos.py", "r", encoding='utf8').read())
exec(open("beallitasok/beallitasok.py", "r", encoding='utf8').read())
exec(open("sorrend/sorrend.py", "r", encoding='utf8').read())

beallitasok_megnyit()

def torles():
    for widgets in frame.winfo_children():
        widgets.destroy()

def vissza():
    torles()
    window.geometry("200x150")
    global ossz
    padx = 60
    width = 10
    label_menu_osszpont = tk.Label(frame, text="Összpont: " + str(ossz), width=width)
    btn_menu_szamolos = tk.Button(frame, text="Számolós", command=szamolos, width=width)
    btn_menu_sorrend = tk.Button(frame, text="Sorrend", command=sorrend, width=width)
    label_menu_ures = tk.Label(frame, text="", width=width)
    btn_menu_beallitasok = tk.Button(frame, text="Beállítások", command=beallitasok, width=width)
    btn_menu_kilepes = tk.Button(frame, text="Kilépés", command=kilepes, width=width)

    label_menu_osszpont.grid(row=0, column=0, padx=padx)
    btn_menu_szamolos.grid(row=1, column=0, padx=padx)
    btn_menu_sorrend.grid(row=2, column=0, padx=padx)
    label_menu_ures.grid(row=3, column=0, padx=padx)
    btn_menu_beallitasok.grid(row=4, column=0, padx=padx)
    btn_menu_kilepes.grid(row=5, column=0, padx=padx)

def kilepes():
    window.destroy()

vissza()

window.mainloop()