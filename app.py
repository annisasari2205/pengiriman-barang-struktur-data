class QueuePengiriman:
    def __init__(self):
        self.antrian = []

    def hitung_ongkir(self, berat):
        ongkir_dasar = 15000
        batas_berat = 5

        if berat > batas_berat:
            kelebihan = berat - batas_berat
            tambahan = kelebihan * 2000
            return ongkir_dasar + tambahan
        else:
            return ongkir_dasar

    def enqueue(self, resi, nama_barang, kategori, berat, penerima, alamat):
        ongkir = self.hitung_ongkir(berat)

        barang = {
            "resi": resi,
            "nama_barang": nama_barang,
            "kategori": kategori,
            "berat": berat,
            "penerima": penerima,
            "alamat": alamat,
            "ongkir": ongkir
        }

        self.antrian.append(barang)
        print("Barang berhasil ditambahkan ke antrian!")

    def dequeue(self):
        if len(self.antrian) == 0:
            print("Antrian kosong!")
        else:
            barang = self.antrian.pop(0)

            print("\n=== BARANG DIKIRIM ===")
            print("No Resi      :", barang["resi"])
            print("Nama Barang  :", barang["nama_barang"])
            print("Kategori     :", barang["kategori"])
            print("Berat        :", barang["berat"], "kg")
            print("Penerima     :", barang["penerima"])
            print("Alamat       :", barang["alamat"])
            print("Total Ongkir : Rp", barang["ongkir"])

    def tampilkan_antrian(self):
        if len(self.antrian) == 0:
            print("Antrian kosong!")
        else:
            print("\n=== DAFTAR ANTRIAN PENGIRIMAN ===")

            for i, barang in enumerate(self.antrian, start=1):
                print(f"\nData Barang #{i}")
                print("No Resi      :", barang["resi"])
                print("Nama Barang  :", barang["nama_barang"])
                print("Kategori     :", barang["kategori"])
                print("Berat        :", barang["berat"], "kg")
                print("Penerima     :", barang["penerima"])
                print("Alamat       :", barang["alamat"])
                print("Total Ongkir : Rp", barang["ongkir"])


# Program Utama
queue = QueuePengiriman()

while True:
    print("\n===== SISTEM PENGIRIMAN BARANG =====")
    print("1. Tambah Barang")
    print("2. Proses Pengiriman")
    print("3. Lihat Antrian")
    print("4. Keluar")

    pilihan = input("Pilih Menu: ")

    if pilihan == "1":
        resi = input("No Resi            : ")
        nama_barang = input("Nama Barang        : ")
        kategori = input("Kategori Barang    : ")
        berat =int(input("Berat Barang (kg)  : "))
        penerima = input("Nama Penerima      : ")
        alamat = input("Alamat Tujuan      : ")

        queue.enqueue(
            resi,
            nama_barang,
            kategori,
            berat,
            penerima,
            alamat
        )

    elif pilihan == "2":
        queue.dequeue()

    elif pilihan == "3":
        queue.tampilkan_antrian()
        
    elif pilihan == "4":
        print("Program selesai, Terimakasih!")
        break

    else:
        print("Pilihan tidak valid!")
