# UI\components.py

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
            font=font,
            cursor=cursor,
            command=command
        )
        self.button.place(x=x, y=y, height=height, width=width)

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
    def get(self):
        return self.ent.get()

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

    def get(self):
        return self.ent.get()

class TextBox:
    def __init__(self, frame, x, y, width, height, text, font=("Arial", 12), state="normal"):
        self.text = tk.Text(
            frame,
            font=font,
            state=state
        )
        self.text.place(x=x, y=y, width=width, height=height)
        self.text.insert(
            index="1.0",
            chars=text
        )

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

class label():
    def __init__(self,frame, text, x, y, font, bg, fg, wl):
        self.label = tk.Label(
            frame,
            text=text,
            font=font,
            bg=bg,
            fg=fg,
            wraplength=wl
        )
        self.label.place(x=x, y=y)
    
    def config(self, text, bg, font):
        self.label.config(
            text=text,
            bg=bg,
            font=font
        )