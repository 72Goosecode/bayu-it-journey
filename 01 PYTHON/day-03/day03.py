# DAY 3 - Python Input Validation, Looping, and Error Handling

# Meminta input tahun sampai pengguna memasukkan angka yang valid
while True:
    try:
        tahun = int(input("Masukkan tahun lahir: "))
        break
    except ValueError:
        print("Input error! Tolong masukkan angka yang benar.")

# Menghitung perkiraan umur
tahun_sekarang = 2026
umur = tahun_sekarang - tahun

# Menampilkan hasil
print(f"Perkiraan umurmu pada tahun {tahun_sekarang} adalah: {umur}")