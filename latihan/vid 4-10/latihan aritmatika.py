# Membuat program untuk melihat suhu reamur, fahrenheit dan kelvin dari input celcius
celcius = float(input("Masukan suhu: "))
print("Suhu", celcius, "Celcius")

reamur = (4 / 5 ) * celcius
print("Suhu", reamur, "Reamur")

fahrenheit = (9 / 5) * celcius +32
print("Suhu", fahrenheit, "fahrenheit")

kelvin = celcius + 273
print("Suhu", kelvin, "kelvin", "\n")



# program melihat suhu celcius, fahrenheit dan kelvin dari input reamur
reamur = float(input("Masukan suhu: "))
print("Suhu", reamur, "reamur")

celcius = (5 / 4) * reamur
print("Suhu", celcius, "celcius")

fahrenheit = (9 / 4) * reamur + 32
print("Suhu", fahrenheit, "fahrenheit")

kelvin = (5 / 4) * reamur + 273
print("Suhu", kelvin, "kelvin\n")



# program melihat suhu celcius, reamur dan kelvin dari input farenheit
fahrenheit = float(input("Masukan suhu: "))
print("Suhu", fahrenheit, "fahrenheit")

celcius = 5/9 * (fahrenheit - 32)
print("Suhu", celcius, "celcius")

reamur = 4/9 * (fahrenheit - 32)
print("Suhu", reamur, "reamur")

kelvin = 5/9 * (fahrenheit - 32) + 273
print("Suhu", reamur, "reamur\n")



# program melihat suhu celcius, reamur dan fahrenheit dari input kelvin
kelvin = float(input("Masukan suhu: "))
print("Suhu", kelvin, "kelvin")

celcius = kelvin - 273
print("Suhu", celcius, "celcius")

reamur = 4/5 * (kelvin - 273)
print("Suhu", reamur, "reamur")

fahrenheit = 9/5 * (kelvin - 273) + 32
print("Suhu", fahrenheit, "fahrenheit")