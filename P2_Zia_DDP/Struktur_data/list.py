buah = ["lengkeng", "melon", "semangka", "pisang"]

#untuk mengaksesnya menggunakan indeks
#indeks dimulai dari 0

#print(buah[0])

#menambah list dengan append()
buah.append("duku")

print(buah)

#mengubah list dengan list[indeks yang diubah] = nilai baru

buah[1] = "duku"
print(buah)

#menghapus list dengan del

del buah[1]
print(buah)

#mengambil data yang paling akhir sekaligus menghapus ==> pop()

print(buah.pop())

#mengetahui jumlah data ==> len()

print(len(buah))

#menyisipkan data sesuai index yang diinginkan

buah.insert(1, "duku")
print(buah)


#mengambil seluruh data di list ==> for

for i in buah:
    #aksi apa yang akan dilakukan?
    #["lengkeng", "melon", "semangka", "pisang"]
    print("buah", i)


#list makanan dengan 2 dimensi
list_makanan = [
    ["bakwan", "tempe", "tahu"],                    #index0
    ["nasi uduk", "nasi pecel", "sate padang"]      #index1
]

#bagaimana memprint nasi pecel?
print(list_makanan[1][1])
#bagaimana memprint semua data?
