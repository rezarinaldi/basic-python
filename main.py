# # Variables
# # Variable adalah tempat untuk menyimpan data. Variable dapat digunakan untuk menyimpan data sementara yang akan digunakan dalam proses pembuatan aplikasi. Variable dapat digunakan untuk menyimpan data berupa angka, string, boolean, dan lain-lain.

# # tidak perlu simbol semicolon di akhir baris
# # python ini termasuk bahasa yang dilihat dari identation-nya (ketika masuk scope), berbeda dari js

# my_name = "Reza"

# # Guide
# # 1. Convention snake_case

# first_name = "Reza"
# last_name = "Rinaldi"

# # 2. Constant (konsisten), ALL_CAPS -> SCREAMING_SNAKE_CASE (kapital semua)
# APP_NAME = "Devscale ID"

# # 3. Start with non-numeric or underscore
# his_name = "Reza"
# _get_name = "Reza"

# first_name = input("Enter your first name: ") # menghasilkan teks/string

# print(first_name)

angka_pertama = input("Masukkan angka pertama: ") # menghasilkan teks/string
angka_kedua = input("Masukkan angka kedua: ") # menghasilkan teks/string

print(int(angka_pertama) + int(angka_kedua)) # int digunakan untuk mengubah teks menjadi angka