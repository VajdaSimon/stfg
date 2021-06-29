def gomb(szam):
    global ossz,eddig,helyes,hibas,sorrend_meret
    for ell in range(0, sorrend_meret * sorrend_meret - 1):
        if eddig == szam and szam == ell:
            eddig += 1
    if eddig == sorrend_meret * sorrend_meret - 1 and szam == sorrend_meret * sorrend_meret - 1:
        ossz = int(ossz) + 1
        open(pontok_spt, "w+").write(str(ossz) + "\n" + str(helyes) + "\n" + str(hibas))
        sorrend()

def sorrend():
    torles()
    
    global ossz,eddig,helyes,hibas,sorrend_meret,sorrend_max
    eddig = 0
    sorrend_meret = int(sorrend_meret)
    
    row = list(range(1,sorrend_meret + 1)) * sorrend_meret
    column = list(range(sorrend_meret)) * sorrend_meret
    
    random.shuffle(row)
    random.shuffle(column)

    szam_min = randint(1, int(sorrend_max))
    
    tk.Label(frame, text="Összpont: " + str(ossz)).grid(row=0, column=0)
    for szam in range(sorrend_meret * sorrend_meret):
        #print("Szám: " + str(szam) + " Row: " + str(row[szam]) + " Column: " + str(column[szam]))
        tk.Button(frame, text=str(szam_min + szam), command=partial(gomb, szam), height=8, width=16).grid(row=row[szam], column=column[szam])
    tk.Button(frame, text="Vissza", command=vissza).grid(row=sorrend_meret + 1, column=0)
    tk.Button(frame, text="Újra töltés", command=sorrend).grid(row=sorrend_meret + 1, column=1)
    window.geometry(str(130 * sorrend_meret) + "x" + str(160 * sorrend_meret))