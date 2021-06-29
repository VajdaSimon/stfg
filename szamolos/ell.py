global helyes,hibas,megoldas,valasz,ossz,pontok_spt
valasz = valasz.get()
def kiiras(sor,szoveg):
        list_of_lines = open(pontok_spt, "r").readlines()
        if sor != 3: 
            list_of_lines[int(sor)] = str(szoveg) + "\n"
        else:
            list_of_lines[int(sor)] = str(szoveg)
        a_file = open(pontok_spt, "w")
        a_file.writelines(list_of_lines)
if str(valasz) == str(megoldas):
    helyes = int(helyes) + 1
    ossz = int(ossz) + 1
    kiiras(2, helyes)
elif str(valasz) != str(megoldas):
    hibas = int(hibas) + 1
    ossz = int(ossz) - 1
    kiiras(3, hibas)
for widgets in frame.winfo_children():
  widgets.destroy()
feladat()