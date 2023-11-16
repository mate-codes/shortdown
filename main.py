import tkinter as tk
import os

def open_shortcuts():
    os.system('python3 shortcut.py &')
    root.destroy()

def shutdown():
    os.system('poweroff')

def restart():
    os.system('reboot')

def log_out():
    os.system('pkill -u $USER')

def cancel():
    root.destroy()

root = tk.Tk()
root.geometry('500x500')
root.resizable(0, 0)
root.title("Shortdown")

button_font = ("Helvetica", 12)

btn_shortcuts = tk.Button(root, text="Shortcuts", command=open_shortcuts, font=button_font)
btn_shutdown = tk.Button(root, text="Shutdown", command=shutdown, font=button_font)
btn_restart = tk.Button(root, text="Restart", command=restart, font=button_font)
btn_log_out = tk.Button(root, text="Log Out", command=log_out, font=button_font)
btn_cancel = tk.Button(root, text="Cancel", command=cancel, font=button_font)

btn_shortcuts.pack(fill=tk.BOTH, expand=True, pady=5)
btn_shutdown.pack(fill=tk.BOTH, expand=True, pady=5)
btn_restart.pack(fill=tk.BOTH, expand=True, pady=5)
btn_log_out.pack(fill=tk.BOTH, expand=True, pady=5)
btn_cancel.pack(fill=tk.BOTH, expand=True, pady=5)

root.mainloop()
