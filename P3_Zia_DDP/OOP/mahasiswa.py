class Mahasiswa:
    nim = ""
    nama = ""
    rombel = ""
    
    def init(self, nim, nama, rombel):
        self.nim = nim
        self.nama = nama
        self.rombel = rombel
    
    def welcome(self):
        print("hallo", self.nama, "Di STT Terpadu Nurul Fikri")
        
    def lulus(self, nilai):
     if(nilai > 90):
        return("lulus")
     else:
        return("tidak lulus")
        
mhs1 = Mahasiswa("0110222024", "Zia", "TI13")
# mhs1.nama = "Zia"
# mhs1.nim = "0110222024"
# mhs1.rombel = "TI13"

print("Nama mahasiswa :", mhs1.nama)
print("nim :", mhs1.nim)
print("rombel :", mhs1.rombel)
print("lulus :", mhs1.lulus)

