import tkinter as tk

window = tk.Tk()

label = tk.Label(text="What's your name?")
entry = tk.Entry()

label.pack()
entry.pack()

name = entry.get()
print(name)

window.mainloop()