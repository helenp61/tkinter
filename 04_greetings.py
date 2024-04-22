import tkinter as tk
from tkinter import ttk


def greet():
    
    # The get() method is used to fetch the value of a                        StringVar() instance.
    # If user_name is empty, print Hello, World!
    # Otherwise, print Hello, <user_name>! 
    #the varibale does not change when the text field changes
    # only used to get the value of the text field
    print(f"Hello, {user_name.get() or 'World'}!")


root = tk.Tk()
root.title("Greeter")

# Here we create an instances of the StringVar() class, which is to track the content of widgets
user_name = tk.StringVar()


name_label = ttk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
#the width property is not in pixels but in number of characters that the field can have.
#the textvariable property is used to bind the StringVar() instance to the Entry widget 

name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)
quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="right", fill="x", expand=True)

root.mainloop()