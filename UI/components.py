import tkinter as tk
from tkinter import ttk


class btn():
    def __init__(self, frame, x, y, width, height, text, color, command):
        self.button = tk.Button(frame, text=text, bg=color, command=command)
        self.button.place(x=x, y=y, height=height, width=width)
        
        