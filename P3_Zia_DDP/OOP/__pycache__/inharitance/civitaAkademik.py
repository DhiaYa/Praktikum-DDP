from Mahasiswa import *
from dosen import *

mhs1 = Mahasiswa("Zia", "Laki-Laki", 18, "Teknik Informatika", 1)
dsn1 = Dosen("Zia","Laki-Laki",18, "S.si, M.kom","Panitia Pesantren Kilat")
mhs1.cetak()
dsn1.cetak()
dsn1.setGaji(500000)