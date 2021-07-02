
# Import Module
from tkinter import *
  
# Create Object
root = Tk()
  
# Set geometry
root.geometry("400x400")
root.configure(bg='white')
  
# Add Image
login_btn = PhotoImage(file = "pottyos/piros.png")
  
# Create button and image
img = Button(root, image = login_btn,
             borderwidth = 0, bg="white")
  
img.pack()
  
# Execute Tkinter
root.mainloop()