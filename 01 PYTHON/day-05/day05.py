angka = input("Masukan angka: ")
hasil = int(angka) + 10
print(hasil)

#input menerima 5 sebagai stirng/teks "5"
#int() merubah string tadi menjadi angka
#jadi python menghitung 5 + 10
#kalau seumpama tidak ada int() maka "5" + "5" = "55"
#print hasil menampilkan program tadi

try:
    angka = int(input("Masukan angka: "))
    print(angka * 2)
except ValueError:
    print("Input tidak valid!")

#Pembahasan beda lagi

while True:
    try:
        angka = int(input("Masukan angka: "))
        print("angka berhasil di diterima!")
        break
    except ValueError:
        print("Input salah, coba lagi!")

    print("Program selesai")

#VALIDASI DATA


while True:
    try:
        nilai = int(input("Masukan angka: "))
        if 0 <= nilai <= 100:
            break
        else:
            print("Nilai harus antara 0 - 100")
    
    except ValueError:
        print("Input harus berupa angka!")

if nilai >= 76:
    hasil = "A"
elif nilai >= 51:
    hasil = "B"
else:
    hasil = "C"

print(f"Nilai yang diterima: {nilai}, dan Hasil ujianmu adalah {hasil}")
