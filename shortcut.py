import tkinter as tk
import os

def terminal():
    os.system('terminal &')
    root.destroy()

def browser():
    os.system('browser &')
    root.destroy()

def explorer():
    os.system('explorer &')
    root.destroy()

root = tk.Tk()
root.geometry('500x500')
root.resizable(0, 0)
root.title("Shortdown")

button_font = ("Helvetica", 12)

button_pkill = tk.Button(root, text="Open Terminal", command=terminal, font=button_font)
button_firefox = tk.Button(root, text="Open Browser", command=browser, font=button_font)
button_thunar = tk.Button(root, text="Open Explorer", command=explorer, font=button_font)

button_pkill.pack(fill=tk.BOTH, expand=True, pady=10)
button_firefox.pack(fill=tk.BOTH, expand=True, pady=10)
button_thunar.pack(fill=tk.BOTH, expand=True, pady=10)

root.mainloop()
