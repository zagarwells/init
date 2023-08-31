class kendaraan:
    def __init__(self, name):
        self.name = name
        self.penumpang = []
    def tambah_penumpang(self, nama_penumpang):
        self.penumpang.append(nama_penumpang)

class mobil(kendaraan):
    pintu_terbuka = False
    def buka_pintu(self):
        self.pintu_terbuka = True
    def tutup_pintu(self):
        self.pintu_terbuka = False
    def welcome(self):
        print("selamat datang! silahkan duduk")

mobil = mobil("mobil tesla")
print(f"nama kendaraan:{mobil.name}")
mobil.tambah_penumpang("ilham")
mobil.tambah_penumpang("abdiel")
mobil.buka_pintu()
print(f"penumpang: {mobil.tambah_penumpang}")
mobil.buka_pintu()
print(f"pintu terbuka: {mobil.pintu_terbuka}")
mobil.tutup_pintu()
print(f"pintu tertutup: {mobil.pintu_terbuka}")
mobil.welcome()