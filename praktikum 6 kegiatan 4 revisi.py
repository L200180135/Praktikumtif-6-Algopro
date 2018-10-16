Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## Kegiatan 4
>>> Nama = 'Anisa Ghoyatul Firdaus'
>>> NIM = 135
>>> Tinggi = 1.52
>>> Berat = 60
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama) # Sebuah tuple
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama] # Sebuah list
>>> type (Aku) # Untuk menampilakan tipe data dari variabel Aku
<type 'tuple'>
>>> Aku [0] # Menampilkan elemen tuple indeks 0
2000
>>> a = NIM % 4 ; Aku [a] # NIM, 135 dibagi dengan 4 sisanya adalah 3. Lalu indeks 3 dimasukkan kedalam variabel Aku
135
>>> type (Aku [a]) # Menampilkan tipe data dari elemen tuple indeks a
<type 'int'>
>>> Aku [a:4] # Slicing dimulai indeks ke 3 dan akhir nya indeks ke 4
(135,)
>>> type (Aku [4]) # Menampilkan tipe data dari elemen tuple indeks 4
<type 'str'>
>>> Aku [0] = 'ok' # ERROR, karena elemen sebuah tuple tidak dapat diubah

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Aku [0] = 'ok' # ERROR, karena elemen sebuah tuple tidak dapat diubah
TypeError: 'tuple' object does not support item assignment
>>> type (Data) # Menampilkan tipe data dari variabel Data
<type 'list'>
>>> type (Data [4]) # Menampilkan tipe data dari elemen list indeks 4
<type 'str'>
>>> Data [4] [5] # Menampilkan list indeks 5 pada list 4
' '
>>> Data [4] [a:6] # Menampilakan list indeks 3 sampai 5 dari list 4
'sa '
>>> Data [0] = 'ok' ; Data # Meubah elemen list pada indeks 0 menjadi ok
['ok', 60, 1.52, 135, 'Anisa Ghoyatul Firdaus']
>>> Data [-a] # Menampilkan indeks sebelum indeks ke 3
1.52
>>> range (a) # Menampilkan list baru pada rentang nilai tertentu
