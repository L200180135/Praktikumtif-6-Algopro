Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Anisa Ghoyatul Firdaus'
>>> NIM = 'L200180135'
>>> x = '1' + NIM [7:] # Didalam string, digabungkan angka 1 dengan slicing yang dimulai dari angka/huruf ke tujuh dari variabel NIM sampai selesai
>>> print (x) # Menampilkan variabel x
1135
>>> a = int (x) # Konversi string ke integer (bilangan bulat)
>>> print (a) # Menampilkan variabel a
1135
>>> b = len (Nama) # Konversi string dalam variabel Nama ke dalam angka
>>> print (b) # Menampilkan variabel b
22
>>> type (a) # Menampilkan type data dari variabel a
<type 'int'>
>>> type (b) # Menampilkan type data dari variabel b
<type 'int'>
>>> a / b # Operasi pembagian antara bilangan dari variabel a dengan b. Type data yang bisa untuk membagi bilangan hanya bila kedua data atau lebih bertype integer/floating point semua dan apabila salah satu data bertype integer sedangkan yang lain dengan type floating point. Data dengan type string tidak bisa diolah menggunakan operasi ini
51
>>> a // b # Operasi pembagian antara bilangan dengan pembulatan ke bawah. Type data yang bisa untuk membagi bilangan hanya bila kedua data atau lebih bertype integer/floating point semua dan apabila salah satu data bertype integer sedangkan yang lain dengan type floating point. Data dengan type string tidak bisa diolah menggunakan operasi ini
51
>>> 10 * (a - 999) # Operasi perkalian ini dapat digunakan untuk mengalikan data dengan type integer dengan integer, floating point dengan floating point, integer dengan floating point, dan dapat juga untuk menggabungkan berulang pada string dengan menggunakan type data integer. Namun, penggabungan berulang kata ini tidak berlaku untuk data dengan type floating point dengan string
1360
>>> b ** 2 # Operasi ini digunakan untuk perpangkatan, type data yang dapat diolah menggunakan operasi ini diantaranya integer dan floating point. Namun, pada operasi ini tidak bisa digunakan untuk menggabungkan ataupun menggabungkan berulang pada sebuah string
484
>>> a % b # Operasi ini digunakan untuk memunculkan sisa hasil bagi
13
>>> c = 12.5 # Variabel c menggunakan angka dengan koma yang berarti type data yang terdapat pada variabel c adalah type floating point
>>> type (c) # Menampilkan type data dari variabel c
<type 'float'>
>>> a / c # Operasi pembagian antara bilangan dari variabel a dengan b. Type data yang bisa untuk membagi bilangan hanya bila kedua data atau lebih bertype integer/floating point semua dan apabila salah satu data bertype integer sedangkan yang lain dengan type floating point. Data dengan type string tidak bisa diolah menggunakan operasi ini
90.8
>>> a // c # Operasi pembagian antara bilangan dengan pembulatan ke bawah. Type data yang bisa untuk membagi bilangan hanya bila kedua data atau lebih bertype integer/floating point semua dan apabila salah satu data bertype integer sedangkan yang lain dengan type floating point. Data dengan type string tidak bisa diolah menggunakan operasi ini
90.0
>>> a % c # Operasi ini digunakan untuk memunculkan sisa hasil bagi
10.0
>>> c > b # Operasi ini digunakan untuk menampilkan perbandingan lebih besar dari. Type dari data adalah boolean
False
>>> type (c > b) # Menampilkan type data dari (c > b)
<type 'bool'>
>>> a > b and b > c # Pada data terdapat dua pernyataan yaitu 1135 > 22 dan 22 > 12.5. Karena, kedua pernyataan tersebut dihubungkan dengan operator logika "and" maka bila kedua pernyataan tersebut bernilai benar maka hasil yang muncul adalah "True", bila salah satu pernyataan salah maka hasil yang muncul pada operasi adalah "False" dan bila kedua pernyataan nya salah maka hasil operasi yang muncul adalah "False"
True
>>> a > 1100 or b < 10 # Logika yang digunakan pada data adalah "or". Dari pernyataan disamping diartikan 1135 > 1100 atau 22 < 10. Dengan 1135 > 1100 adalah data pertama dan 22 < 10 sebagai data kedua.  Hasil dari operasi disamping bernilai "True" karena menggunakan logika "atau". Apabila kedua data bernilai benar maka "True", salah satu dari data bernilai benar maka "True" namun apabila kedua data bernilai salah maka "False" yang akan muncul pada hasil operasi
True
>>> 
