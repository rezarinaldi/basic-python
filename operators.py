# Operator adalah simbol khusus yang digunakan untuk melakukan operasi tertentu pada suatu nilai atau variable.

# Arithmetic Operators (Aritmatika)
# Addition +
result = 1 + 2

# Subtraction -
result = 2 - 1

# Multiplication *
result = 2 * 3

# Division /
result = 4 / 3 # float

# Floor Division //
result = 4 // 3

# Modulus % (reminder) 
result = 10 % 3

# Exponent (**) -> pangkat
result = 4 ** 3
# print(result)

# Comparison Operators (Perbandingan) -> Boolean
# == (equal)
value_a = 10
value_b = 3
# result = value_a == value_b # False

# != (not equal)
# result = value_a != value_b # True

# > (greater than)
# result = value_a > value_b # True

# < (less than)
# result = value_a < value_b # False

# >= (greater than or equal)
# result = value_a >= value_b # True

# <= (less than or equal)
# result = value_a <= value_b # False

# Logical Operators (Logika) -> 2 buah Boolean
# AND -> && -> and (Returning True if Both are True), keduanya harus sama agar True
x = "admin"
y = "admin"
a = 1
b = 2
# result = x == y and a == b

# OR -> || -> or (Returning True if either are True), cukup salah satu saja
# result = x == y or a == b

# Identity Operators (Identitas)
# Sebuah perbandingan yang mengecek sebuah variabel, apakah mengacu pada objek yang sama.

# is -> True if both variables are the same object
value_a = None # class

# result = value_a is None # apakah dia mengacu pada class tertentu -> True

# is not -> True if variables both are not same or different object

value_b = None # class

result = value_b is not None # apakah dia tidak mengacu pada class tertentu -> False

print(result)
