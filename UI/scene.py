# UI\scene.py

import tkinter as tk
from tkinter import ttk

class Scene():
    def __init__(self):
        self.scene = tk.Tk()
        self.scene.geometry("720x480")
        self.scene.title("The Everything Translator")

    def run(self):
        self.scene.mainloop()