#Augusta Clarissa Silvy Pascalin
#Universitas Kristen Duta Wacana
#Topik : Modular Programming

'''Adel mendapat tugas dari guru matematikanya untuk membuat jaring-jaring tabung. Karena Adel sudah terlanjur
menentukan besar volume dan radiusnya, maka Ia kebingungan untuk menentukan tinggi yang pas. Buat program
untuk menghitung tinggi tabung agar tugas Adel cepat selesai!'''

#input : r, V
#proses : def, rumus, menghitung rumus
#output : tinggi tabung

def tinggiTabung(V,r):
        return (3.14*(r**2))/V 
r = float(input("Masukkan radius tabung : "))
V = float(input("Masukkan volume tabung (>= radius) : "))
print("Tinggi tabung yang harus dibuat Adel", tinggiTabung(V,r), "cm")