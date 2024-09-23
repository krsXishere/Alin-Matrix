import tkinter as tk
from tkinter import messagebox
import sympy as sp

# Fungsi untuk mengambil input matriks dari Entry secara dinamis
def input_matrix(matrix_num):
    try:
        rows = int(input_baris.get())
        cols = int(input_kolom.get())
        matrix = []
        if matrix_num == 1:
            entries = entry_matrix1
        else:
            entries = entry_matrix2
            
        for i in range(rows):
            row_input = entries[i]
            row = list(map(float, row_input.get().split()))
            if len(row) != cols:
                raise ValueError(f"Jumlah kolom pada baris {i+1} tidak sesuai.")
            matrix.append(row)
        return sp.Matrix(matrix)
    except Exception as e:
        messagebox.showerror("Error", f"Kesalahan input: {e}")
        return None

# Fungsi untuk menampilkan hasil dalam bentuk matriks di window
def tampilkan_hasil(hasil):
    for widget in frame_hasil.winfo_children():
        widget.destroy()

    label_hasil = tk.Label(frame_hasil, text="Hasil Operasi Matriks:", font=('Arial', 14), fg="white", bg="#34495E")
    label_hasil.pack(pady=10)

    text_hasil = tk.Text(frame_hasil, height=10, width=50, font=('Courier', 12), bg="#ECF0F1")
    text_hasil.pack()

    # Format hasil ke bentuk matriks
    hasil_str = str(hasil)
    text_hasil.insert(tk.END, hasil_str)

# Fungsi untuk memproses pilihan operasi
def proses_operasi(pilihan):
    matrix1 = input_matrix(1)
    if matrix1 is None:
        return
    
    try:
        if pilihan in ['Penjumlahan', 'Pengurangan', 'Perkalian']:
            matrix2 = input_matrix(2)  # Ambil matriks kedua untuk operasi
            if matrix2 is None:
                return
            if pilihan == 'Penjumlahan':
                hasil = matrix1 + matrix2
            elif pilihan == 'Pengurangan':
                hasil = matrix1 - matrix2
            elif pilihan == 'Perkalian':
                hasil = matrix1 * matrix2
        elif pilihan == 'Transpose':
            hasil = matrix1.transpose()
        elif pilihan == 'Determinan':
            hasil = matrix1.det()
        elif pilihan == 'Invers':
            hasil = matrix1.inv()
        elif pilihan == 'Trace':
            hasil = matrix1.trace()
        else:
            hasil = "Operasi tidak dikenal."
        
        # Tampilkan hasil di window
        tampilkan_hasil(hasil)

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Fungsi untuk menampilkan input matriks dinamis untuk satu atau dua matriks
def generate_matrix_input(jumlah_matriks):
    try:
        rows = int(input_baris.get())
        cols = int(input_kolom.get())

        # Bersihkan entry matrix sebelumnya
        for widget in frame_matriks.winfo_children():
            widget.destroy()

        global entry_matrix1, entry_matrix2
        entry_matrix1, entry_matrix2 = [], []

        # Generate input untuk matriks pertama
        label_matriks1 = tk.Label(frame_matriks, text="Matriks 1:", bg="#34495E", fg="white")
        label_matriks1.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        for i in range(rows):
            label = tk.Label(frame_matriks, text=f"Baris {i+1}: ", bg="#34495E", fg="white")
            label.grid(row=i+1, column=0, padx=5, pady=5)
            entry = tk.Entry(frame_matriks, width=50, bg="#ECF0F1")
            entry.grid(row=i+1, column=1, padx=5, pady=5)
            entry_matrix1.append(entry)

        # Jika operasi membutuhkan dua matriks, buat input untuk matriks kedua
        if jumlah_matriks == 2:
            label_matriks2 = tk.Label(frame_matriks, text="Matriks 2:", bg="#34495E", fg="white")
            label_matriks2.grid(row=rows+1, column=0, padx=5, pady=5, columnspan=2)
            for i in range(rows):
                label = tk.Label(frame_matriks, text=f"Baris {i+1}: ", bg="#34495E", fg="white")
                label.grid(row=rows+2+i, column=0, padx=5, pady=5)
                entry = tk.Entry(frame_matriks, width=50, bg="#ECF0F1")
                entry.grid(row=rows+2+i, column=1, padx=5, pady=5)
                entry_matrix2.append(entry)

    except ValueError:
        messagebox.showerror("Error", "Masukkan jumlah baris dan kolom yang valid.")

# Fungsi untuk menampilkan halaman operasi
def halaman_operasi(jumlah_matriks):
    frame_menu.pack_forget()
    frame_operasi.pack()
    generate_matrix_input(jumlah_matriks)

# Fungsi untuk menampilkan halaman pembuka
def halaman_pembuka():
    frame_operasi.pack_forget()
    frame_menu.pack()

# Inisialisasi window utama
window = tk.Tk()
window.title("Program Operasi Matriks")
window.geometry("600x750")
window.configure(bg="#2C3E50")

# Frame halaman pembuka
frame_menu = tk.Frame(window, bg="#2C3E50")
frame_menu.pack()

label_title = tk.Label(frame_menu, text="Selamat Datang di Program Operasi Matriks", font=('Arial', 16, 'bold'), bg="#2C3E50", fg="white")
label_title.pack(pady=20)

btn_penjumlahan = tk.Button(frame_menu, text="Penjumlahan", command=lambda: halaman_operasi(2), font=('Arial', 14), bg='#2980B9', fg='white', width=20)
btn_penjumlahan.pack(pady=10)

btn_pengurangan = tk.Button(frame_menu, text="Pengurangan", command=lambda: halaman_operasi(2), font=('Arial', 14), bg='#2980B9', fg='white', width=20)
btn_pengurangan.pack(pady=10)

btn_perkalian = tk.Button(frame_menu, text="Perkalian", command=lambda: halaman_operasi(2), font=('Arial', 14), bg='#2980B9', fg='white', width=20)
btn_perkalian.pack(pady=10)

btn_transpose = tk.Button(frame_menu, text="Transpose", command=lambda: halaman_operasi(1), font=('Arial', 14), bg='#9B59B6', fg='white', width=20)
btn_transpose.pack(pady=10)

btn_determinan = tk.Button(frame_menu, text="Determinan", command=lambda: halaman_operasi(1), font=('Arial', 14), bg='#9B59B6', fg='white', width=20)
btn_determinan.pack(pady=10)

btn_invers = tk.Button(frame_menu, text="Invers", command=lambda: halaman_operasi(1), font=('Arial', 14), bg='#9B59B6', fg='white', width=20)
btn_invers.pack(pady=10)

btn_trace = tk.Button(frame_menu, text="Trace", command=lambda: halaman_operasi(1), font=('Arial', 14), bg='#9B59B6', fg='white', width=20)
btn_trace.pack(pady=10)

# Frame halaman operasi
frame_operasi = tk.Frame(window, bg="#2C3E50")

label_input_baris = tk.Label(frame_operasi, text="Masukkan jumlah baris: ", bg="#2C3E50", fg="white")
label_input_baris.pack(pady=5)
input_baris = tk.Entry(frame_operasi, bg="#ECF0F1")
input_baris.pack()

label_input_kolom = tk.Label(frame_operasi, text="Masukkan jumlah kolom: ", bg="#2C3E50", fg="white")
label_input_kolom.pack(pady=5)
input_kolom = tk.Entry(frame_operasi, bg="#ECF0F1")
input_kolom.pack()

# Frame untuk memasukkan elemen matriks
frame_matriks = tk.Frame(frame_operasi, bg="#2C3E50")
frame_matriks.pack(pady=10)

btn_kembali = tk.Button(frame_operasi, text="Kembali", command=halaman_pembuka, font=('Arial', 12), bg='red', fg='white', width=20)
btn_kembali.pack(pady=20)

btn_proses = tk.Button(frame_operasi, text="Proses", font=('Arial', 14), bg='#27AE60', fg='white', width=20, command=lambda: proses_operasi(selected_operation.get()))
btn_proses.pack(pady=10)

# Frame hasil
frame_hasil = tk.Frame(window, bg="#34495E")
frame_hasil.pack(fill=tk.BOTH, expand=True)

# Inisialisasi global variabel matriks
entry_matrix1 = []
entry_matrix2 = []

window.mainloop()
