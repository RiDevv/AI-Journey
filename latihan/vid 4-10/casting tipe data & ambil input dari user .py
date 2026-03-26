# kita akan melakukan perubah tipe data 1 menjadi tipe data lain nya
print("==== Merubah Int ke tipe data lain ====")
int_to_float = float(5)
print(int_to_float, "bertipe data", type(int_to_float))

int_to_string = str(5)
print(int_to_string, "bertipe data", type(int_to_string))

int_to_boolean = bool(5) #jika 0 maka False jika selain 0 True
print(int_to_boolean, "bertipe data", type(int_to_boolean), "\n")


print("==== Merubah Float ke tipe data lain ====")
float_to_int = int(5.9) # akan di bulatkan ke bawah
print(float_to_int, "bertipe data", type(float_to_int))

float_to_string = str(5.9)
print(float_to_string, "bertipe data", type(float_to_string))

float_to_bool = bool(5.9) # sama kaya int selain 0 akan true dan 0 akan false
print(float_to_bool, "bertipe data", type(float_to_bool), "\n")


print("==== Merubah String ke tipe data lain")
string_to_int = int(10) #string yang hanya berisi angka yang bisa di ubah menjadi float atau integer
print(string_to_int, "bertipe data", type(string_to_int))

string_to_bool = bool("Hallo") #string kosong = False, string berisi = True
print(string_to_bool, "bertipe data", type(string_to_bool), "\n")


print("==== Merubah Boolean ke tipe data lain ====")
bool_to_int = int(False) # Dalam int False = 0, True = 1. dalam float False = 0.0, True = 1.0
print(bool_to_int, "bertipe data", type(bool_to_int))

bool_to_string = str(False)
print(bool_to_string, "bertipe data", type(bool_to_string), "\n")



# Ambil input dari user
nama = input("Masukan nama lengkap anda: ")
print("Hallo, Selamat datang", nama, "!")

# Sesimpel itu cara mengambil input dari user
# buat variabel untuk menyimpan inputan dari user