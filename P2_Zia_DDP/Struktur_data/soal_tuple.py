gorengan = ("bakwan", "combro", "misro")                #index0
sop = ("sop iga", "sop buntut", "sop kaki")             #index1
nasi = ("nasi uduk", "nasi goreng", "nasi rames")       #index2

#tuple didalam tuple
makanan = (gorengan, sop, nasi)
#cetak gorengan saja
print(makanan[0])
for i in makanan[0]:
    print(i)

#cetak sop buntu
print(makanan[1][1])

#cetak nasi rames
print(makanan[2][2])

#cetak semuanya dan keluarkan dari buka tutup kurung
for i in makanan:
    for detail in i:
        print(detail)