global helyes,hibas,megoldas,valasz,ossz,pontok_spt
valasz = valasz.get()
if str(valasz) == str(megoldas):
    helyes = int(helyes) + 1
    ossz = int(ossz) + 1
    open(pontok_spt, "w+").write(str(ossz) + "\n" + str(helyes) + "\n" + str(hibas))
elif str(valasz) != str(megoldas):
    hibas = int(hibas) + 1
    ossz = int(ossz) - 1
    open(pontok_spt, "w+").write(str(ossz) + "\n" + str(helyes) + "\n" + str(hibas))
for widgets in frame.winfo_children():
  widgets.destroy()
pontok()
feladat()