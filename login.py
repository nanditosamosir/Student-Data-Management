import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

from data_management import *
from main import *

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Manajemen Data mahasiswa")

        self.frame = ttk.Frame(root)
        self.frame.pack(ipadx=10,ipady=10,fill="x")

        self.username_label = tk.Label(self.frame, text="Username:")
        self.username_label.grid(column=0,row=0,pady=5)

        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(column=1,row=0,pady=5)

        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.grid(column=0,row=1,pady=5)

        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(column=1,row=1,pady=5)

        self.login_button = tk.Button(self.frame, text="Login", command=self.login)
        self.login_button.grid(column=1,row=2,pady=10,padx=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        #cek login
        if self.check_login(username, password):
            messagebox.showinfo("Login Success", "Welcome, {}".format(username))
            self.root.destroy()

            root_main = tk.Tk()
            root_main.geometry('800x600')
            app_main = MainApp(root_main)
            root_main.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def check_login(self, username, password):
        #read data csv
        with open('Proyek/login.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == username and row[1] == password:
                    return True
        return False
