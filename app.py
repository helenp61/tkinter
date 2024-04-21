import tkinter as tk
from tkinter import ttk

#for widgets and buttons

root = tk.Tk()   #the main window
ttk.Label(root, text="Hello World!", padding=(30, 10)).pack()
#label will be inside the main root(parent) and then telling it to pack itself into the parent
#pack is a geometry manager that tells the widget to be packed into the parent


root.mainloop()

