# Exceptions
# Metode untuk meng-handling sebuah error.
# Kalau dalam js itu try-catch, kalau dalam python itu try-except

value = "0"

try:
  if value == "0":
    raise TypeError("Not a valid type")
  if value == 0:
    raise Exception("Not valid value") 
    # untuk nge-return sebuah exception, yang kemudian nantinya akan ditangkap oleh exception-nya
except TypeError as e:
  print(f"Error Type: {e}")
except Exception as e:
# except di sini fungsinya adalah untuk menerima atau menangkap exception yang ada di-raise/return (diminta)
# kemudian, kita akan menerima berbagai macam exception class,
# value error exception, not found exception, dsb
# Exception yang ada di atas disebut generic exception 
  print(f"Exception: {e}")
# dengan punya exception yang baik, maka bisa melakukan handling error secara gracefully dengan artian kalau ada error tidak sampai bikin aplikasinya break total