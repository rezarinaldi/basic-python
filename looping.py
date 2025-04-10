# Looping
# Sebuah istilah untuk membuat sebuah bahasa pemrograman itu bisa melakukan perulangan pada sebuah data (bagaimana sebuah data itu bisa dimanipulasi).

# fruits = ["banana", "durian","cherry"]

# for fruit in fruits:
#   print(fruit)

# di atas ini termasuk for loop
# fruit: satu variabel untuk menampung setiap single value-nya
# fruits: iterable object (list, tuple, atau semisalnya)

# Break
# Sebuah keyword untuk keluar dari sebuah perulangan

# for fruit in fruits:
#   if fruit == "durian ":
#     continue # skip
#     # break # keluar dari perulangan, sisanya tidak akan diproses
#   print(fruit)

# for index, fruit in enumerate(fruits, 1): # menghasilkan tuple
#   print(index, fruit)

# While Loop
# Kondisi perulangan ketika sebuah kondisi masih terpenuhi

condition = True

while condition:
  user_input = input("Masukkan secret: ")
  if user_input == "admin":
    condition = False

# akan terus berulang jika kondisi belum terpenuhi (False)
# berhenti ketika mendapatkan kondisi yang terpenuhi (True)