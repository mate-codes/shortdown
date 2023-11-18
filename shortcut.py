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
root.configure(bg='#FFFFFF') 

button_font = ("Helvetica", 12)

button_terminal = tk.Button(root, text="Open Terminal", command=terminal, font=button_font, bg='#FFFFFF', fg='black', bd=2, highlightbackground='#FFFFFF', activebackground='#FFFFFF')
button_browser = tk.Button(root, text="Open Browser", command=browser, font=button_font, bg='#FFFFFF', fg='black', bd=2, highlightbackground='#FFFFFF', activebackground='#FFFFFF')
button_explorer = tk.Button(root, text="Open Explorer", command=explorer, font=button_font, bg='#FFFFFF', fg='black', bd=2, highlightbackground='#FFFFFF', activebackground='#FFFFFF')

button_terminal.pack(fill=tk.BOTH, expand=True, pady=10)
button_browser.pack(fill=tk.BOTH, expand=True, pady=10)
button_explorer.pack(fill=tk.BOTH, expand=True, pady=10)

root.mainloop()
