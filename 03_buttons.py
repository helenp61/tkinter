import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello, World!")


root = tk.Tk()
root.title("Hello")

greet_button = ttk.Button(root, text="Greet", command=greet)
#pass in a text and commands
#command is a function that will be called when the button is pressed
#fill makes the button expand to fill the entire width of the parent
#expand makes the button expand to fill the entire height of the parent
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand=True)  # could use side="right"

root.mainloop()