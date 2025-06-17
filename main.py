import tkinter as tk
from tkinter import ttk, Canvas
import ttkbootstrap as ttk

# window
window = ttk.Window(themename="journal")
window.title("Guess the number")
window.geometry("400x400")

# title
title_label = ttk.Label(window, text="Guess the number:",font="Calibri 24 bold")
title_label.pack()


# run
window.mainloop()