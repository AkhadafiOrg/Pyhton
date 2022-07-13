""" ==========Number========== """
# Variabel tipe numerik dibuat saat Anda menetapkan nilai padanya:
x = 1  # int
y = 2.8  # float
z = 1j  # complex

# Untuk memverifikasi jenis objek apa pun dengan Python, gunakan fungsi type() :
print(type(x))
print(type(y))
print(type(z))

# Int, atau bilangan bulat, adalah bilangan bulat, positif atau negatif, tanpa desimal, dengan panjang tak terbatas.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float, atau "angka titik mengambang" adalah angka, positif atau negatif, yang mengandung satu atau lebih desimal.
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Bilangan kompleks ditulis dengan "j" sebagai bagian imajiner:
x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
""" ==========Number========== """


""" ==========Conversion========== """
# Anda dapat mengonversi dari satu jenis ke jenis lainnya dengan metode int(), float(), dan complex():
# Konversi dari satu jenis ke jenis lainnya:
x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
""" ==========Conversion========== """


""" ==========Random Number========== """
# Python tidak memiliki fungsi random() untuk membuat angka acak, tetapi Python memiliki modul bawaan yang disebut random yang dapat digunakan untuk membuat angka acak:
# Impor modul acak, dan tampilkan nomor acak antara 1 dan 9:
import random

print(random.randrange(1, 10))
""" ==========Random Number========== """
