varakozik = ""
def beallitasok():
    torles()
    window.geometry("235x210")
    global terminal,checkbtn_terminal_uj,varakozik
    global szamolos_max,szamolos_min,szamolos_max_uj,szamolos_min_uj
    global sorrend_meret,sorrend_max,scale_sorrend_uj,entry_sorrend_max_uj
    label_beallitasok = tk.Label(frame, text="Beállítások")
    
    if varakozik != "":
        tk.Label(frame, text=varakozik).grid(row=0, column=2)

    label_terminal = tk.Label(frame, text="Terminál:")
    if int(terminal) == 0:
        btn_terminal_uj = tk.Button(frame, text="Kikapcsolás", command=terminal_ki)
    if int(terminal) == 1:
        btn_terminal_uj = tk.Button(frame, text="Bekapcsolás", command=terminal_be)


    label_szamolos = tk.Label(frame, text="Számolós:")
    label_szamolos_min = tk.Label(frame, text="Min.")
    szamolos_min_uj = tk.Entry(frame, textvariable=StringVar(window, value=szamolos_min))
    label_szamolos_max = tk.Label(frame, text="Max.")
    szamolos_max_uj = tk.Entry(frame, textvariable=StringVar(window, value=szamolos_max))
    
    label_sorrend = tk.Label(frame, text="Sorrend:")
    label_sorrend_meret = tk.Label(frame, text="Méret:")
    scale_sorrend_uj = tk.Scale(frame, from_=2, to=5, orient=HORIZONTAL)
    scale_sorrend_uj.set(sorrend_meret)
    label_sorrend_max = tk.Label(frame, text="Max.")
    entry_sorrend_max_uj = tk.Entry(frame, textvariable=StringVar(window, value=sorrend_max))
    btn_nullazas = tk.Button(frame, text="Idők nullázása", command=nullazas)
    
    btn_mentes = tk.Button(frame, text="Mentés", command=mentes)
    btn_vissza = tk.Button(frame, text="Vissza", command=vissza)
    btn_alap = tk.Button(frame, text="Alapbeállítások", command=alap)
    
    label_beallitasok.grid(row=0, column=0)
    
    label_terminal.grid(row=1, column=0)
    btn_terminal_uj.grid(row=1, column=2)

    label_szamolos.grid(row=2, column=0)
    label_szamolos_min.grid(row=2, column=1)
    szamolos_min_uj.grid(row=2, column=2)
    label_szamolos_max.grid(row=3, column=1)
    szamolos_max_uj.grid(row=3, column=2)
    
    label_sorrend.grid(row=4, column=0)
    label_sorrend_meret.grid(row=4, column=1)
    scale_sorrend_uj.grid(row=4, column=2)
    label_sorrend_max.grid(row=5, column=1)
    entry_sorrend_max_uj.grid(row=5, column=2)
    btn_nullazas.grid(row=6, column=2)

    btn_mentes.grid(row=8, column=0)
    btn_vissza.grid(row=8, column=1)
    btn_alap.grid(row=8, column=2)
    
def sikeres():
        tk.Label(frame, text="Mentve!").grid(row=0, column=2)

def terminal_ki():
    beallitasok_kiiras(4,1)
    global varakozik
    varakozik = "Újra indításra vár!"
    tk.Label(frame, text="Újra kell indítani!").grid(row=0, column=2)

def terminal_be():
    beallitasok_kiiras(4,0)
    global varakozik
    varakozik = "Újra indításra vár!"
    tk.Label(frame, text="Újra kell indítani!").grid(row=0, column=2)

def mentes():
    global szamolos_max,szamolos_min,szamolos_max_uj,szamolos_min_uj
    global sorrend_meret,sorrend_max,scale_sorrend_uj,entry_sorrend_max_uj
    szamolos_min_uj = str(szamolos_min_uj.get())
    szamolos_max_uj = str(szamolos_max_uj.get())
    scale_sorrend_uj = str(scale_sorrend_uj.get())
    entry_sorrend_max_uj = str(entry_sorrend_max_uj.get())
    if str(szamolos_min) != szamolos_min_uj and szamolos_min_uj != "":
        beallitasok_kiiras(0,szamolos_min_uj)
        sikeres()
    if str(szamolos_max) != szamolos_max_uj and szamolos_max_uj != "":
        beallitasok_kiiras(1,szamolos_max_uj)
        sikeres()
    if str(sorrend_meret) != scale_sorrend_uj and scale_sorrend_uj != "":
        beallitasok_kiiras(2,scale_sorrend_uj)
        sikeres()
    if str(sorrend_max) != entry_sorrend_max_uj and entry_sorrend_max_uj != "":
        beallitasok_kiiras(3,entry_sorrend_max_uj)
        sikeres()
    beallitasok_megnyit()
    beallitasok()

def alap():
    beallitasok_kiiras(0,str(-5))
    beallitasok_kiiras(1,15)
    beallitasok_kiiras(2,2)
    beallitasok_kiiras(3,20)
    beallitasok_megnyit()
    beallitasok()
    sikeres()

def nullazas():
    for sor in range(4):
        sorrend_best_ido_kiiras(sor, "x")
        sorrend_best_ido[sor] = "x"