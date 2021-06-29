def gomb(szam):
    global ossz,eddig,helyes,hibas,sorrend_meret,sorrend_pontok,gomb_felirat,szam_min
    for ell in gomb_felirat:
        if eddig == szam and szam == ell:
            eddig += 1
    if eddig == szam_min + sorrend_meret * sorrend_meret and szam + 1 == szam_min + sorrend_meret * sorrend_meret:
        ossz = int(ossz) + 1
        sorrend_pontok = int(sorrend_pontok) + 1
        open(pontok_spt, "w+").write(str(ossz) + "\n" + str(helyes) + "\n" + str(hibas)  + "\n" + str(sorrend_pontok))
        sorrend()

def sorrend():
    torles()
    global ossz,eddig,helyes,hibas,sorrend_meret,sorrend_max,sorrend_pontok
    sorrend_meret = int(sorrend_meret)

    maxr = sorrend_meret
    maxc = sorrend_meret
    
    global gomb_felirat,szam_min
    szam_min = randint(1, int(sorrend_max))
    gomb_felirat = list(range(szam_min, szam_min + sorrend_meret * sorrend_meret))
    random.shuffle(gomb_felirat)

    eddig = szam_min

    label_osszpont = tk.Label(frame, text="Összpont: " + str(ossz))
    label_pontok = tk.Label(frame, text="Pontok: " + str(sorrend_pontok))
    for szam in range(sorrend_meret * sorrend_meret):
        tk.Button(frame, text=str(gomb_felirat[szam]), command=partial(gomb, gomb_felirat[szam]), height=8, width=16).grid(row=int(szam // maxr + 1), column=int(szam % maxr))
    btn_vissza = tk.Button(frame, text="Vissza", command=vissza)
    #btn_ujratoltes = tk.Button(frame, text="Újra töltés", command=sorrend)
    window.geometry(str(130 * sorrend_meret) + "x" + str(160 * sorrend_meret))

    label_osszpont.grid(row=0, column=0)
    label_pontok.grid(row=0, column=1)
    #Játék gombok helye
    btn_vissza.grid(row=sorrend_meret + 1, column=0)
    #btn_ujratoltes.grid(row=sorrend_meret + 1, column=1)