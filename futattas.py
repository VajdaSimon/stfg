import tkinter as tk
from tkinter import *
from random import randint
from functools import partial
import random

window = tk.Tk()

def gomb(szam):
    print(str(szam))

def sorrend():
    verzio = 3
    
    row = [0,1,0,1]
    column = [0,0,1,1]
    random.shuffle(row)
    random.shuffle(column)

    szam_min = randint(1, 10)
    
    print(row)
    print(column)

    for szam in range(4):
        tk.Button(text=str(szam_min + szam), command=partial(gomb, szam), height=8, width=16, font=1).pack()  #.grid(row=row[szam], column=column[szam])

# tk.Button(text="2", command=lambda: gomb(2), height=8, width=16).grid(row=1, column=0)
# tk.Button(text="3", command=lambda: gomb(3), height=8, width=16).grid(row=0, column=1)
# tk.Button(text="4", command=lambda: gomb(4), height=8, width=16).grid(row=1, column=1)

sorrend()

window.mainloop()