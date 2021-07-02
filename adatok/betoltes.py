hely = "adatok/pontok.spt"
f = open(hely, "a+")
if os.stat(hely).st_size == 0:
    f = open(hely, "a")
    f.write("0\n0\n0\n0")
f = open(hely, "r")
f = f.read()
ossz,helyes,hibas,sorrend_pontok = f.split("\n")

hely = "adatok/beallitasok.spt"
f = open(hely, "a+")
if os.stat(hely).st_size == 0:
    f = open(hely, "a")
    f.write("-5\n10\n2\n20")
def beallitasok_megnyit():
    f = open(hely, "r")
    f = f.read()
    global szamolos_min,szamolos_max,sorrend_meret,sorrend_max
    szamolos_min,szamolos_max,sorrend_meret,sorrend_max = f.split("\n")

hely = "adatok/sorrend_best_ido.spt"
f = open(hely, "a+")
if os.stat(hely).st_size == 0:
    f = open(hely, "a")
    f.write("x\nx\nx\nx")
f = open(hely, "r")
f = f.read()
sorrend_best_ido = f.split("\n")
