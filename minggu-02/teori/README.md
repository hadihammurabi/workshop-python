# More Control Flow Tools

Sebagai bahasa pemrograman, Python dapat melakukan kegiatan tertentu berdasarkan kondisi tertentu. Hal ini juga dapat dilakukan pada bahasa pemrograman lainnya.

## Pernyataan `if`

Perintah/pernyataan `if` digunakan untuk melakukan sebuah aktivitas atau lebih sesuai dengan kondisi tertentu.

Contoh:

Menampilkan _output_ dengan kondisi tertentu.

```python
nilai = 100

if nilai > 85:
    print('kamu pintar sekali')
elif nilai > 75:
    print('bagus')
else:
    print('belajar lagi ya')
```

## Pernyataan `for`

Perulangan juga merupakan salah satu aktivitas _standard_ yang dapat dilakukan di bahasa pemrograman pada umumnya, termasuk Python. Untuk melakukan perulangan, dapat dilihat pada contoh berikut.

```python
animals = ['cat', 'dog', 'chicken']
for animal in animals:
    print(animal, len(animal))
```

## Fungsi `range()`

Fungsi `range()` merupakan sebuah fungsi yang ada di Python. Fungsi ini dapat digunakan untuk mendapatkan baris angka.

Penggunaannya sebagai berikut.

`range(min, max, [step])`

Contoh:

Menampilkan _list_ angka dari 1 sampai 9.

```python
print(list(range(1, 10)))
```

Fungsi range ini juga dapat digunakan pada perulangan `for`.

Contoh:

```python
for num in range(1, 10):
    print(num)
```

## Pernyataan `break` dan `continue`

Kedua pernyataan ini dapat dilakukan di dalam sebuah perulangan, misalkan `for`.

`break` digunakan untuk keluar dari perulangan sehingga perulangan tidak dilanjutkan.

`continue` digunakan untuk melewatkan sekali perulangan tetapi masih dilanjutkan.



Contoh:

Memberhentikan perulangan apabila sudah lebih dari 5 kali.

```python
for num in range(1, 10):
    if num > 5:
        break
    print(num)
```

Melewati perulangan ke-5.

```python
for num in range(1, 10):
    if num == 5:
        continue
    print(num)
```

