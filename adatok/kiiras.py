def beallitasok_kiiras(sor,szoveg):
    hely = "adatok/beallitasok.spt"
    file = open(hely, "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    list_of_lines = open(hely, "r").readlines()
    if sor != line_count - 1: 
        list_of_lines[int(sor)] = str(szoveg) + "\n"
    else:
        list_of_lines[int(sor)] = str(szoveg)
    a_file = open(hely, "w")
    a_file.writelines(list_of_lines)

def pontok_kiiras(sor,szoveg):
    hely = "adatok/pontok.spt"
    file = open(hely, "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    list_of_lines = open(hely, "r").readlines()
    if sor != line_count - 1: 
        list_of_lines[int(sor)] = str(szoveg) + "\n"
    else:
        list_of_lines[int(sor)] = str(szoveg)
    a_file = open(hely, "w")
    a_file.writelines(list_of_lines)

def sorrend_best_ido_kiiras(sor,szoveg):
    hely = "adatok/sorrend_best_ido.spt"
    file = open(hely, "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    list_of_lines = open(hely, "r").readlines()
    if sor != line_count - 1: 
        list_of_lines[int(sor)] = str(szoveg) + "\n"
    else:
        list_of_lines[int(sor)] = str(szoveg)
    a_file = open(hely, "w")
    a_file.writelines(list_of_lines)