# membuat list
buah = ['jeruk', 'apel', 'mangga', 'apel']

print(buah) # output: ['jeruk', 'apel', 'mangga']

# menghitung banyaknya data yang ada pada sebuah list
print(len(buah)) # output: 4

# menghitung banyaknya data tertentu pada sebuah list
print(buah.count('apel')) # output: 2

# membalik urutan data
buah_copy = [b for b in buah] 
buah_copy.reverse()

print(buah_copy) # output: ['apel', 'mangga', 'apel', 'jeruk']

# menambah data
buah.append('salak')

print(buah) # output: ['jeruk', 'apel', 'mangga', 'apel', 'salak']

# mengurutkan data berdasarkan alfabet
buah_copy = [b for b in buah]
buah_copy.sort()
print(buah_copy) # output: ['apel', 'apel', 'jeruk', 'mangga', 'salak']

# mengambil sebuah data dan menghapusnya
buah_copy = [b for b in buah]
buah_diambil = buah_copy.pop()

print(buah_diambil) # output: salak
print(buah_copy) # output: ['jeruk', 'apel', 'mangga', 'apel']

