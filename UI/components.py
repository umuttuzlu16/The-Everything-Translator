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
        self.ent.pack()

class combo():
    def __init__(self, frame, x, y, text, values, state):
        self.ent = tk.StringVar()
        self.ent = ttk. Combobox(
            frame,
            textvariable=text,
            values=values,
            state=state
        )
        self.ent.place(x=x, y=y)


class TextBox:
    def __init__(self, frame, x, y, width, height, font=("Arial", 12), state="normal"):
        self.text = tk.Text(
            frame,
            width=width,
            height=height,
            font=font,
            state=state
        )
        self.text.place(x=x, y=y)

    def get(self):
        return self.text.get("1.0", tk.END).strip()

    def set(self, content):
        self.text.config(state="normal")
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", content)
        self.text.config(state="disabled")

    def enable(self):
        self.text.config(state="normal")

    def disable(self):
        self.text.config(state="disabled")