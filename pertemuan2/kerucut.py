# program aplikasi menghitung luas dan volume kerucut

# Pertemuan 2
# Programmer: Nana handre saputra
# Tanggal:  11 November 2023

import tkinter as tk
import math

def calculate():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())
        volume = (1/3) * math.pi * (jari_jari ** 2) * tinggi
        luas_permukaan = math.pi * jari_jari * (jari_jari + math.sqrt((jari_jari ** 2) + (tinggi ** 2)))
        label_volume.config(text="Volume Kerucut: {:.2f}".format(volume))
        label_luas_permukaan.config(text="Luas Permukaan Kerucut: {:.2f}".format(luas_permukaan))
    except ValueError:
        label_volume.config(text="Masukkan bilangan valid")
        label_luas_permukaan.config(text="")

root = tk.Tk()
root.title("Kalkulator Kerucut")
root.geometry("250x250")

label_jari_jari = tk.Label(root, text="Jari-Jari Alas Kerucut:")
label_jari_jari.pack()
entry_jari_jari = tk.Entry(root)
entry_jari_jari.pack()

label_tinggi = tk.Label(root, text="Tinggi Kerucut:")
label_tinggi.pack()
entry_tinggi = tk.Entry(root)
entry_tinggi.pack()

calculate_button = tk.Button(root, text="Hitung", command=calculate)
calculate_button.pack()

label_volume = tk.Label(root, text="")
label_volume.pack()
label_luas_permukaan = tk.Label(root, text="")
label_luas_permukaan.pack()

root.mainloop()

