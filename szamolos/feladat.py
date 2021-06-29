global sze,szm,megoldas,valasz,szamolos_min,szamolos_max,ossz,helyes,hibas
label_szamolos_pontok = tk.Label(frame, text="Összpont: " + str(ossz) + "\nEddig helyesen megoldva: " + str(helyes) + "\n" + "Eddig hibássan megoldva: " + str(hibas))

padx = 20
width = 10

sze = randint(int(szamolos_min), int(szamolos_max))
szm = randint(int(szamolos_min), int(szamolos_max))
megoldas = sze + szm

feladat = tk.Label(frame, text=str(sze) + "+" + str(szm) + "=")
valasz = tk.Entry(frame)
valasz.focus()
gomb = tk.Button(frame, text="Tovább", command=ell, width=width)
vissza = tk.Button(frame, text="Vissza", command=vissza, width=width)

label_szamolos_pontok.grid(row=0, column=0, padx=padx) 
feladat.grid(row=1, column=0, padx=padx)
valasz.grid(row=2, column=0, padx=padx)
gomb.grid(row=3, column=0, padx=padx)
vissza.grid(row=4, column=0, padx=padx)