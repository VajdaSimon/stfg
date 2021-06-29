def gomb(szam):
    global ossz,eddig,helyes,hibas,sorrend_meret,sorrend_pontok
    for ell in range(0, sorrend_meret * sorrend_meret - 1):
        if eddig == szam and szam == ell:
            eddig += 1
    if eddig == sorrend_meret * sorrend_meret - 1 and szam == sorrend_meret * sorrend_meret - 1:
        ossz = int(ossz) + 1
        sorrend_pontok = int(sorrend_pontok) + 1
        open(pontok_spt, "w+").write(str(ossz) + "\n" + str(helyes) + "\n" + str(hibas)  + "\n" + str(sorrend_pontok))
        sorrend()

def sorrend():
    torles()
    
    global ossz,eddig,helyes,hibas,sorrend_meret,sorrend_max,sorrend_pontok
    eddig = 0
    sorrend_meret = int(sorrend_meret)
    
    row = list(range(1,sorrend_meret + 1)) * sorrend_meret
    column = list(range(sorrend_meret)) * sorrend_meret
    
    random.shuffle(row)
    random.shuffle(column)

    szam_min = randint(1, int(sorrend_max))
    
    label_osszpont = tk.Label(frame, text="Összpont: " + str(ossz))
    label_pontok = tk.Label(frame, text="Pontok: " + str(sorrend_pontok))
    for szam in range(sorrend_meret * sorrend_meret):
        tk.Button(frame, text=str(szam_min + szam), command=partial(gomb, szam), height=8, width=16).grid(row=row[szam], column=column[szam])
    btn_vissza = tk.Button(frame, text="Vissza", command=vissza)
    btn_ujratoltes = tk.Button(frame, text="Újra töltés", command=sorrend)
    window.geometry(str(130 * sorrend_meret) + "x" + str(160 * sorrend_meret))

    label_osszpont.grid(row=0, column=0)
    label_pontok.grid(row=0, column=1)
    #Játék gombok helye
    btn_vissza.grid(row=sorrend_meret + 1, column=0)
    btn_ujratoltes.grid(row=sorrend_meret + 1, column=1)