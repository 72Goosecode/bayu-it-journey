#Tugas Day 2
#Meminta nama pengguna dengan input().
#Meminta pekerjaan pengguna dengan input().
#Menampilkan kalimat perkenalan menggunakan f-string.

nama = input("Siapa namamu? ")
work = input("Apa pekerjaanmu? ")

print(f"Namaku adalah {nama} dan Pekerjaanku adalah {work}")

#Meminta tahun lahir dengan input().
#Mengubah masukan menjadi integer menggunakan int().
#Menghitung perkiraan umur berdasarkan tahun 2026.
#Menampilkan hasilnya menggunakan f-string.

tahun_lahir = int(input("Masukan tahun lahirmu "))
tahun_sekarang = int(input("Masukan tahun sekarang "))

umur = tahun_sekarang - tahun_lahir

print(f"Umurku di tahun {tahun_sekarang} ini adalah {umur}")

#Evaluasi hari ini setelah input kasih spasi agar lebih bagus tampilannya
#Untuk input yang berupa data string apabila case nya "5" + "5" outputnya adalah "55"
#Namun untuk int(input(text)) seumpama di isi 5 + 5 outputnya adalah 10
#Dan untuk string + integer hasilnya akan error
#lalu apabila di case ada variabel seperti ini
# tahun_lahir = 2030 - 1997
# print(tahun_lahir) outputnya akan tereksekusi 33 karena data yang dibaca disitu integer
#Contoh case

tahun_now = 2030 - 4
lahir = int(input("Masukan tahun lahirmu: "))

print(tahun_now - lahir + 1) #Outputnya akan menjadi 30