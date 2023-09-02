from video_module_2 import cleaned_string
import tkinter as tk
import re


value = cleaned_string.cleaned_string

window = tk.Tk()
window.title("License Plate Recognition")
window.resizable(False, False)
window.geometry("1500x750+10+10")

label = tk.Label(window, text=value)
label.place(x = 100,y = 100)

window.mainloop()