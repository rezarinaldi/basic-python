# Function
# Sebuah module atau bagian dari program yang dapat dijalankan secara terpisah dan dapat digunakan kembali atau berkali-kali di mana saja dalam program.
def say_hello(name, age):
    return f"Hello {name}! your age is {age}"  # return digunakan untuk mengembalikan nilai (ketika sebuah function dipanggil)


my_hello = say_hello("Reza", 25)
# print(my_hello)

## Day 2
# Input & Output
# def say_hi(name):
#     print(f"Hello {name}!")

# result = say_hi("Reza")
# print(result) # None (mengacu pada class) atau Null, tidak ada yang dikembalikan

# def say_hi(name):
#     return f"Hello {name}!"

# result = say_hi("Reza")
# print(result)

# def sum(x, y):
#     return x + y

# result_a = sum(1, 2) # penjumlahan
# result_b = sum(result_a, 2)
# print(result_a)
# print(result_b)

# Args with asterisk symbol
# Parameter yang memungkinkan sebuah function untuk menerima number of positional arguments

def say_name(*args):
    name_1, name_2, name_3 = args # Destructure dari Tuple
    print(f"Name: {name_1}, {name_2}, {name_3}")

# say_name("Reza", "Jessy", "Rifa")

# Kwagrs with asterisk symbol
# Parameter yang memungkinkan sebuah function untuk menerima number of keyword arguments (ada key, ada value)

def say_names(**kwargs):
    # name_a = kwargs["name_d"] # UNSAFE, jika mengambil sesuatu yang tidak ada
    name = kwargs.get("name_x", None) # SAFE, akan mengembalikan None jika tidak ada
    print(name)
    pass

say_names(name_a="Reza", name_b="Jessy", name_c="Rifa")

# Args rules
# regular, with_default=value, *args, and **kwargs
# harus berurutan, tidak boleh terbalik

def sample(regular, with_default="value", *args, **kwargs):
    print(regular)
    print(with_default)
    print(args[0])
    print(kwargs.get("my_input"))
    pass