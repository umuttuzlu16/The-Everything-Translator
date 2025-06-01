import tkinter as tk
from tkinter import ttk


class btn():
    def __init__(self, frame, x, y, width, height, text, bg, command, fg, activebackground, activeforeground, font, cursor):
        self.button = tk.Button(
            frame,
            text=text,
            bg=bg,
            fg=fg,
            activebackground=activebackground,
            activeforeground=activeforeground,
            font=font,   # font=24 hatalıydı, tuple formatında olmalı
            height=height,
            width=width,
            cursor=cursor,
            command=command
        )
        self.button.place(x=x, y=y)

class ent():
    def __init__(self, frame, width, string, index):
        self.ent = tk.Entry(
            frame,
            width=width,
        )
        self.ent.insert(
            string=string,
            index=index
        )