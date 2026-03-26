x = 8
y = 5

# penjumlahan
penjumlahan = x + y
print(x, "+", y, "=", penjumlahan)

# pengurangan
pengurangan = x - y
print(x, "-", y, "=", pengurangan)

# perkalian
perkalian = x * y
print(x, "*", y, "=", perkalian)

# pembagian (jika angka di bagi akan menghasilkan tipe data float)
pembagian = x / y
print(x, "/", y, "=", pembagian)

# pembagian yang di bulatkan jika hasilnya koma
pembagian2 = x // y
print(x, "//", y, "=", pembagian2)

# pangkat
pangkat = x ** y
print(x, "**", y, "=", pangkat)

# modulus (sisa bagi)
mod = x % y
print(x, "%", y, "=", mod)



# Nah disini kita bisa mencoba materi casting tipe data
# yaitu saat pengambilan input dari user yang mengirim angka
# secara default walaupun yang dikirim angka dia bertipe data string
# kita akan ubah menjadi integer karena akan digunakan untuk operasi aritmatika / kalkulator penjumlahan
angka1 = int(input("Masukan angka pertama: "))
angka2 = int(input("Masukan angka kedua: "))
hasil = angka1 + angka2

print("Hasil penjumlahan dari", angka1, "dan", angka2, "adalah", hasil)