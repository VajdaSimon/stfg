def feladat():
    exec(open("szamolos/feladat.py", "r", encoding='utf8').read())

def ell():
    exec(open("szamolos/ell.py", "r", encoding='utf8').read())
    
def ell2(event):
    ell()    
window.bind('<Return>', ell2)

def szamolos():
    for widgets in frame.winfo_children():
        widgets.destroy()
    window.geometry("210x150")
    feladat()