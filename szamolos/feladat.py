global sze,szm,megoldas,valasz,szamolos_min,szamolos_max
sze = randint(int(szamolos_min), int(szamolos_max))
szm = randint(int(szamolos_min), int(szamolos_max))
megoldas = sze + szm
feladat = tk.Label(frame, text=str(sze) + "+" + str(szm) + "=")
valasz = tk.Entry(frame)
valasz.focus()
gomb = tk.Button(frame, text="Tovább", command=ell)
vissza = tk.Button(frame, text="Vissza", command=vissza)
    
feladat.pack()
valasz.pack()
gomb.pack()
vissza.pack()