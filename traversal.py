# Traversal
# Sebuah istilah untuk mengakses, atau melakukan examination, atau memanipulasi dari data yang ada.
# my_name = "Reza Rinaldi"

# print(len(my_name)) # len digunakan untuk menghitung panjang string
# print(my_name[0]) # indexing -> mengambil value dari string
# print(my_name[-1])

# print(my_name.upper()) # mengubah string menjadi huruf besar
# print(my_name.lower()) # mengubah string menjadi huruf kecil
# print(my_name.capitalize()) # mengubah string menjadi huruf awalannya besar
# print(my_name.title()) # mengubah string menjadi huruf awalannya besar (setiap perubahan kata yang dipisahkan oleh spasi)

her_name = "Jessy mencari takjil"

# print(her_name.replace("takjil", "jodoh")) # bisa merubah dari satu buah kata di dalam sebuah string dengan kata yang lain

my_name = "Reza Rinaldi"
# print(my_name[0:2]) # Slicing adalah mengambil karakter pada posisi tertentu [start:end] -> Re
# print(my_name[:4]) # [start:end] -> Reza
# print(my_name[::2]) # [start:end:step] -> Reza
# # step: mengambil karakter pada posisi tertentu berdasarkan step-nya (dihitung dari awal) -> Rz iad
# print(my_name[:1:2]) # -> R

# Format
my_text = """
My name is {name}
I live at {city}.
"""

my_recipe = """
Generate a recipe with ingredients: {ingredients}
"""

# print(my_recipe.format(ingredients="milk, beef, and tomato"))

# F-String -> Literal template kalau dalam js
my_name = "Reza"
my_next_text = f"My name is {my_name}"

print(my_next_text)