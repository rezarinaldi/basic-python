# Control Flow
# Skema if else. Sebuah istilah untuk membuat sebuah bahasa pemrograman itu bisa menentukan operasi apa yang akan diterapkan kepada sebuah data (bagaimana sebuah data itu bisa dimanipulasi).

# grade = 85

# if grade > 90:
#   print("Grade A+")
# elif grade > 80 and grade <= 90:
#   print("Grade B")
# else:
#   print("Not a Grade A+")

# Example,
def check_grades(grade: int):
  if grade >= 90:
    print("Grade A")
  elif grade >= 80:
    print("Grade B")
  elif grade >= 70:
    print("Grade C")
  elif grade >= 60:
    print("Grade D")
  else:
    print("Grade E")

check_grades(90) # Grade A