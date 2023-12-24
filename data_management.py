import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

from login import *
from login import *

class MainApp():
    def __init__(self,root):
        self.root = root
        self.root.title('Sistem Manajemen Data Mahasiswa')

        self.frame = ttk.Frame(root)
        self.frame.pack(ipadx=10,ipady=10,fill="x")

        self.showData_button = tk.Button(self.frame,text='1.Show All Data',command=self.showData)
        self.showData_button.grid(column=0,row=0,pady=5)

        self.deleteData_button = tk.Button(self.frame, text='2.Delete Data', command=self.selected_delete_data)
        self.deleteData_button.grid(column=0,row=1,sticky='w',columnspan=2)

        self.addData_button = tk.Button(self.frame, text='3.Add Data', command=self.add_data)
        self.addData_button.grid(column=0, row=2, pady=5,sticky='w')

        self.replaceData_button = tk.Button(self.frame, text='4.Replace Data', command=self.replace_data)
        self.replaceData_button.grid(column=0, row=3, pady=5,sticky='w')

        self.inputNilai_button = tk.Button(self.frame, text='5.Input Nilai', command=self.input_nilai)
        self.inputNilai_button.grid(column=0, row=4, pady=5,sticky='w')

        self.avgNilai_button = tk.Button(self.frame, text='6.Calculate Avg Nilai', command=self.calculate_avg_nilai)
        self.avgNilai_button.grid(column=0, row=5,sticky='w',pady=5)

        self.exit_button = tk.Button(self.frame,text='7.Exit',command=exit)
        self.exit_button.grid(column=0,row=6,sticky='w',pady=5)

        self.table_frame = ttk.Frame(root)

        self.table = ttk.Treeview(self.table_frame, columns=("NIM", "Nama", "Nilai Ujian 1", "Nilai Ujian 2", "Nilai Ujian 3"), show="headings")
        self.table.heading("NIM", text="NIM")
        self.table.heading("Nama", text="Nama")
        self.table.heading("Nilai Ujian 1", text="Nilai Ujian 1")
        self.table.heading("Nilai Ujian 2", text="Nilai Ujian 2")
        self.table.heading("Nilai Ujian 3", text="Nilai Ujian 3")
        

        self.populate_table_from_csv("Proyek/presensi.csv")
    
    def showData(self):
        new_root = tk.Toplevel(self.root)
        new_root.title("Main Menu")
        new_root.geometry('1040x400')
        new_root.title("Main Menu")

        # Membuat tabel pertama
        self.table_frame = ttk.Frame(new_root)
        self.table_frame.grid(row=0, column=0, padx=10, pady=10)

        self.isi1 = tk.Label(new_root,text='Back to Menu :')
        self.isi1.grid(column=0,row=1,padx=5,pady=5)
        
        self.yes_button = tk.Button(new_root,text='Yes',command=new_root.destroy)
        self.yes_button.grid(column=0,row=2,padx=10,pady=5)


        self.table = ttk.Treeview(self.table_frame, columns=("NIM", "Nama", "Nilai Ujian 1", "Nilai Ujian 2", "Nilai Ujian 3"), show="headings")
        self.table.heading("NIM", text="NIM")
        self.table.heading("Nama", text="Nama")
        self.table.heading("Nilai Ujian 1", text="Nilai Ujian 1")
        self.table.heading("Nilai Ujian 2", text="Nilai Ujian 2")
        self.table.heading("Nilai Ujian 3", text="Nilai Ujian 3")
        self.table.pack()

        # Mengisi tabel dengan data dari file CSV
        self.populate_table_from_csv("Proyek/presensi.csv")

    def populate_table_from_csv(self, csv_file):
        try:
            with open(csv_file, newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader)  # Mengambil header dari CSV

                # Menentukan indeks kolom NIM, Nama, Nilai Ujian 1, Nilai Ujian 2, dan Nilai Ujian 3
                nim_index = header.index("NIM")
                nama_index = header.index("NAMA")
                nilai_ujian1_index = header.index("Nilai Ujian 1")
                nilai_ujian2_index = header.index("Nilai Ujian 2")
                nilai_ujian3_index = header.index("Nilai Ujian 3")

                # Mengisi tabel dengan data dari CSV
                for row in reader:
                    try:
                        nim = row[nim_index]
                        nama = row[nama_index]
                        nilai_ujian1 = row[nilai_ujian1_index]
                        nilai_ujian2 = row[nilai_ujian2_index]
                        nilai_ujian3 = row[nilai_ujian3_index]
                        self.table.insert("", "end", values=(nim, nama, nilai_ujian1, nilai_ujian2, nilai_ujian3))
                    except IndexError:
                        print(f"Baris {reader.line_num}: Jumlah elemen tidak sesuai, lewati baris ini.")

        except FileNotFoundError:
            print(f"File {csv_file} tidak ditemukan.")

    def selected_delete_data(self):
        new_root = tk.Toplevel(self.root)
        new_root.title('Select Data')
        new_root.geometry('1040x400')
        new_root.title("Select Data")

        self.frame = ttk.Frame(new_root)
        self.frame.pack(ipadx=10,ipady=10,fill="x")

        self.deleteData_button = tk.Button(self.frame, text='Delete Data', command=self.delete_data)
        self.deleteData_button.grid(column=0,row=1,sticky='w',columnspan=2)

        
        self.table_frame = ttk.Frame(new_root)
        self.table_frame.pack(padx=10, pady=10)

        self.table = ttk.Treeview(self.table_frame, columns=("NIM", "Nama", "Nilai Ujian 1", "Nilai Ujian 2", "Nilai Ujian 3"), show="headings")
        self.table.heading("NIM", text="NIM")
        self.table.heading("Nama", text="Nama")
        self.table.heading("Nilai Ujian 1", text="Nilai Ujian 1")
        self.table.heading("Nilai Ujian 2", text="Nilai Ujian 2")
        self.table.heading("Nilai Ujian 3", text="Nilai Ujian 3")
        self.table.pack()

        self.populate_table_from_csv("Proyek/presensi.csv")
        
    def delete_data(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Delete Data", "No data selected. Please select a row.")
            return

        # Get the name from the selected row
        name_to_delete = self.table.item(selected_item, "values")[1]

        # Ask for confirmation before deletion
        confirmation = messagebox.askyesno("Delete Data", f"Do you want to delete the data for {name_to_delete}?")
        if confirmation:
            # Perform the deletion from the CSV file
            self.delete_data_from_csv("Proyek/presensi.csv", name_to_delete)
            # Refresh the table after deletion
            self.populate_table_from_csv("Proyek/presensi.csv")
        root.destroy()
    def delete_data_from_csv(self, csv_file, name_to_delete):
        rows_to_keep = []
        try:
            with open(csv_file, 'r', newline='', encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader)

                # Find the index of the 'Nama' column
                nama_index = header.index("NAMA")

                # Keep only rows where the 'Nama' column is not equal to the name to delete
                rows_to_keep = [row for row in reader if row[nama_index] != name_to_delete]

        except FileNotFoundError:
            print(f"File {csv_file} not found.")

        # Write the updated rows back to the CSV file
        with open(csv_file, 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows_to_keep)

    def add_data(self):
        nim = self.get_input("Masukkan NIM:")
        nama = self.get_input("Masukkan Nama:")

        if nim and nama:
            self.append_data_to_csv("Proyek/presensi.csv", nim, nama)
            self.populate_table_from_csv("Proyek/presensi.csv")
        else:
            messagebox.showwarning("Add Data", "NIM dan Nama tidak boleh kosong.")

    def get_input(self, prompt):
        top = tk.Toplevel(self.root)

        label = tk.Label(top, text=prompt)
        label.pack(pady=5)

        entry_var = tk.StringVar()
        entry = tk.Entry(top, textvariable=entry_var)
        entry.pack(pady=5)

        def submit():
            result = entry_var.get()
            top.destroy()
            return result

        button = tk.Button(top, text="OK", command=submit)
        button.pack(pady=5)

        top.wait_window()
        return entry_var.get()
    
    def append_data_to_csv(self, csv_file, nim, nama):
        try:
            with open(csv_file, 'a', newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([nim, nama, "", "", ""])
        except FileNotFoundError:
            print(f"File {csv_file} not found.")

    def input_nilai(self):
        nim = self.get_input("Masukkan NIM Mahasiswa:")
        nilai_ujian1 = self.get_input("Masukkan Nilai Ujian 1:")
        nilai_ujian2 = self.get_input("Masukkan Nilai Ujian 2:")
        nilai_ujian3 = self.get_input("Masukkan Nilai Ujian 3:")

        if nim and nilai_ujian1 and nilai_ujian2 and nilai_ujian3:
            self.update_nilai_in_csv("Proyek/presensi.csv", nim, nilai_ujian1, nilai_ujian2, nilai_ujian3)
            self.populate_table_from_csv("Proyek/presensi.csv")
        else:
            messagebox.showwarning("Input Nilai", "Semua input harus diisi.")

    def update_nilai_in_csv(self, csv_file, nim, nilai_ujian1, nilai_ujian2, nilai_ujian3):
        try:
            rows = []
            with open(csv_file, 'r', newline='', encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader)

                nim_index = header.index("NIM")
                nilai_ujian1_index = header.index("Nilai Ujian 1")
                nilai_ujian2_index = header.index("Nilai Ujian 2")
                nilai_ujian3_index = header.index("Nilai Ujian 3")

                for row in reader:
                    if row[nim_index] == nim:
                        row[nilai_ujian1_index] = nilai_ujian1
                        row[nilai_ujian2_index] = nilai_ujian2
                        row[nilai_ujian3_index] = nilai_ujian3
                    rows.append(row)

            with open(csv_file, 'w', newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(rows)

        except FileNotFoundError:
            print(f"File {csv_file} not found.")

    def calculate_avg_nilai(self):
        nim = self.get_input("Masukkan NIM Mahasiswa untuk menghitung rata-rata nilai:")
        if nim:
            avg_nilai = self.calculate_avg_nilai_for_nim("Proyek/presensi.csv", nim)
            if avg_nilai is not None:
                messagebox.showinfo("Average Nilai", f"Rata-rata nilai untuk NIM {nim}: {avg_nilai:.2f}")
            else:
                messagebox.showerror("Average Nilai", f"Tidak dapat menemukan NIM {nim} pada data.")
        else:
            messagebox.showwarning("Average Nilai", "NIM harus diisi.")

    def calculate_avg_nilai_for_nim(self, csv_file, nim):
        try:
            with open(csv_file, 'r', newline='', encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader)

                nim_index = header.index("NIM")
                nilai_ujian1_index = header.index("Nilai Ujian 1")
                nilai_ujian2_index = header.index("Nilai Ujian 2")
                nilai_ujian3_index = header.index("Nilai Ujian 3")

                total_nilai = 0
                count = 0

                for row in reader:
                    if row[nim_index] == nim:
                        nilai_ujian1 = float(row[nilai_ujian1_index]) if row[nilai_ujian1_index] else 0
                        nilai_ujian2 = float(row[nilai_ujian2_index]) if row[nilai_ujian2_index] else 0
                        nilai_ujian3 = float(row[nilai_ujian3_index]) if row[nilai_ujian3_index] else 0

                        total_nilai += (nilai_ujian1 + nilai_ujian2 + nilai_ujian3)/3
                        count += 1

                if count > 0:
                    avg_nilai = total_nilai / count
                    return avg_nilai
                else:
                    return None

        except FileNotFoundError:
            print(f"File {csv_file} not found.")

    def replace_data(self):
        nama_lama = self.get_input("Masukkan Nama Lama:")
        nim_lama = self.get_input("Masukkan NIM Lama:")
        nama_baru = self.get_input("Masukkan Nama Baru:")
        nim_baru = self.get_input("Masukkan NIM Baru:")

        if nama_lama and nim_lama and nama_baru and nim_baru:
            if self.replace_data_in_csv("Proyek/presensi.csv", nim_lama, nama_lama, nim_baru, nama_baru):
                messagebox.showinfo("Replace Data", "Data berhasil diganti.")
                self.populate_table_from_csv("Proyek/presensi.csv")
            else:
                messagebox.showerror("Replace Data", "Data tidak ditemukan.")
        else:
            messagebox.showwarning("Replace Data", "Semua input harus diisi.")

    def replace_data_in_csv(self, csv_file, nim_lama, nama_lama, nim_baru, nama_baru):
        try:
            rows = []
            with open(csv_file, 'r', newline='', encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader)

                nim_index = header.index("NIM")
                nama_index = header.index("NAMA")

                for row in reader:
                    if row[nim_index] == nim_lama and row[nama_index] == nama_lama:
                        row[nim_index] = nim_baru
                        row[nama_index] = nama_baru
                    rows.append(row)

            with open(csv_file, 'w', newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(rows)

            return True

        except FileNotFoundError:
            print(f"File {csv_file} not found.")
            return False
        
    
    def exit(self):
        root.destroy()
        messagebox.showinfo(message='Berhasil Keluar')
        