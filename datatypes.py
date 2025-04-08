# Data Types (Tipe Data)
# Sebuah istilah untuk membuat sebuah bahasa pemrograman itu bisa menentukan operasi apa yang akan diterapkan kepada sebuah data (bagaimana sebuah data itu bisa dimanipulasi).

# Numeric Data Types
# Numeric data types digunakan untuk menyimpan angka.
# integer (Whole Number): 1,2,5,233,293
my_age = 25
# float (Decimal): 1.5, 2.5, 3.14
my_phi = 3.14

result = my_age + my_phi # > Float
# print(result)

# String
my_name = "Reza" # single line
my_address = """
Malang, East Java, Indonesia
""" # multi line

# print(my_address)

# Boolean -> True or False (pakai huruf besar)
# untuk control flow
is_reza_student = True
is_rifa_mentor = False

# Sequence (list of value atau array) -> mutable, non-fixed size
fruits = ["banana", "durian","cherry"]
fruits.append("avocado")

# print(fruits)

# Tuple -> immutable, fixed size (Sequence yang tidak bisa diubah dan size tetap sama)
coordinate = (0,1)

# print(coordinate)

# Range
my_range = range(5) # 0,5
my_list = list(my_range) # 0,1,2,3,4

# print(my_list)

# Dictionary -> key-value pairs data
user = {
  "name": "Reza",
  "age": 25,
  "is_student": True
}

# print(user)
# print(user["name"])
print(user.get("sports")) # None atau Null