import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

from login import *
from data_management import *


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x400')
    app = LoginApp(root)
    root.mainloop()