import tkinter as tk
from tkinter import ttk

class Scene():
    def __init__(self):
        self.scene = tk.Tk()
        self.scene.geometry("1080x720")
        self.scene.title("The Everything Translator")

    def run(self):
        self.scene.mainloop