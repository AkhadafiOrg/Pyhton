""" ==========Python Variables========== """
x = 5
y = "Khadafi"
print(x)
print(y)

x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)

x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0


# Casting
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0


# Get the Type
x = 5
y = "Khadafi"
print(type(x))
print(type(y))


# Single or Double Quotes?
x = "Khadafi"
# is the same as
x = "Khadafi"


# Case-Sensitive
a = 4
A = "Sally"
# A will not overwrite a
""" ==========Python Variables========== """


""" ==========Variable Names========== """
"""
Sebuah variabel dapat memiliki nama pendek (seperti x dan y) atau nama yang lebih deskriptif (umur, carname, total_volume). Aturan untuk variabel Python:
  * Nama variabel harus dimulai dengan huruf atau karakter garis bawah
  * Nama variabel tidak boleh diawali dengan angka
  * Nama variabel hanya boleh berisi karakter alfanumerik dan garis bawah (A-z, 0-9, dan _ )
  * Nama variabel peka huruf besar/kecil (usia, Usia, dan AGE adalah tiga variabel berbeda)
"""

myvar = "Khadafi"
my_var = "Khadafi"
_my_var = "Khadafi"
myVar = "Khadafi"
MYVAR = "Khadafi"
myvar2 = "Khadafi"

# Camel Case
myVariableName = "Khadafi"
# Pascal Case
MyVariableName = "Khadafi"
# Snake Case
my_variable_name = "Khadafi"
""" ==========Variable Names========== """


""" ==========Assign Multiple Values========== """
# Many Values to Multiple Variables
# Python memungkinkan Anda untuk menetapkan nilai ke beberapa variabel dalam satu baris:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
# Dan Anda dapat menetapkan nilai yang sama ke beberapa variabel dalam satu baris:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# Jika Anda memiliki kumpulan nilai dalam daftar, tuple dll. Python memungkinkan Anda untuk mengekstrak nilai ke dalam variabel. Ini disebut membongkar.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
""" ==========Assign Multiple Values========== """


""" ==========Output Variables========== """
# Fungsi Python print() sering digunakan untuk menghasilkan variabel.
x = "Python is awesome"
print(x)

# Dalam fungsi print(), Anda menampilkan beberapa variabel, dipisahkan dengan koma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Anda juga dapat menggunakan operator + untuk menampilkan beberapa variabel:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Untuk angka, karakter + berfungsi sebagai operator matematika:
x = 5
y = 10
print(x + y)

# Cara terbaik untuk menampilkan beberapa variabel dalam fungsi print() adalah dengan memisahkannya dengan koma, yang bahkan mendukung tipe data yang berbeda:
x = 5
y = "John"
print(x, y)
""" ==========Output Variables========== """


""" ==========Global Variables========== """
# Global Variables
# Variabel global dapat digunakan oleh semua orang, baik di dalam fungsi maupun di luar.
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

# Global Variables
# Jika Anda membuat variabel dengan nama yang sama di dalam suatu fungsi, variabel ini akan bersifat lokal, dan hanya dapat digunakan di dalam fungsi tersebut. Variabel global dengan nama yang sama akan tetap seperti semula, global dan dengan nilai aslinya.
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)

# The global Keyword
# Biasanya, ketika Anda membuat variabel di dalam suatu fungsi, variabel itu bersifat lokal, dan hanya dapat digunakan di dalam fungsi itu.
# Untuk membuat variabel global di dalam suatu fungsi, Anda dapat menggunakan kata kunci global.
def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

# The global Keyword
# Untuk mengubah nilai variabel global di dalam suatu fungsi, lihat variabel tersebut dengan menggunakan kata kunci global:
x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
""" ==========Global Variables========== """
