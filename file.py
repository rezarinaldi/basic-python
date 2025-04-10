from maths import sum, subtract # cara melakukan importing module
# import maths
from libs.data import display_data

result = sum(2, 3)
result = subtract(10, 7)

display_data(result) 

# ketika menjalankannya, kita mendapatkan satu folder bernama __pycache__
# bisa disebut name mangling, sebuah variabel, file, atau class yang diubah menjadi private (tidak boleh dipanggil di luar dari instansi class tersebut)
# fungsinya, untuk merubah dari module yang telah dijalankan, di-compile menjadi bytecode (code interpreter) -> yang menerjemahkan dari pythoncode ke bytecode (bisa dieksekusi lebih cepat oleh mesin)
# folder __pycache__ tidak boleh dihapus, tapi bisa di-hide