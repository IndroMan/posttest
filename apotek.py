# =================================================
# =====================DATABASE====================
# =================================================
# Dictionary daftar obat yang dijual beserta harganya

import datetime as dt
import json
import os

# Membuka file database.json
try:
    with open('database.json') as f:
        # Memasukkan isi file database.json ke variabel obat
        obat = json.load(f)
except FileNotFoundError:  # Jika tidak ada database.json
    obat = {
    "Paracetamol": 20000,
    "Vitamin C": 1000,
    "Sianida XXL": 30000
    }

# Variabel keranjang belanja
pesanan = []
kuantitas = []

# Fungsi untuk me-refresh database
def refresh_database():
    # Memanggil variabel global obat dan id_obat
    global obat
    global id_obat
    
    # Mengurutkan dictionary berdasarkan alfabet keys
    obat = dict(sorted(obat.items()))
    
    with open("database.json", "w") as f:  
        json.dump(obat, f)
    
    # Membuat dictionary berdasarkan angka dari 1
    # dengan value dari keys obat
    # Contoh:
    # obat = {
    #     "Paracetamol": 20000,
    #     "Vitamin C": 1000,
    #     }
    # id_obat = {
    #     1: "Paracetamol",
    #     2: "Vitamin C"
    #     }
    id_obat = dict()
    id_obat.clear()
    for i in range(len(obat)):
        id_obat[i+1] = list(dict.keys(obat))[i]

# Fungsi untuk mengubah angka menjadi format uang:
# 40000 => Rp40.000,-
duit = lambda a: 'Rp' + format(a,',d').replace(',','.') + ',-'


# =================================================
# ======================MENU=======================
# =================================================
# Menu
def menu_awal():
    # Menghapus keranjang belanja
    pesanan.clear()
    kuantitas.clear()
    
    # Mencetak pilihan menu
    print()
    print("=" * 40)
    print("  APOTEK GAMAUSAKIT  ".center(40, "="))
    print("  MENU  ".center(40, "="))
    print(f"  {str(dt.date.today())}  ".center(40, "=")) 
    print("=" * 40)
    print("1) Beli Obat\n"
          "2) Daftar Obat\n"
          "3) Admin\n"
          "0) Keluar\n")
    print("Pilih perintah!")
    
    # Looping jika pilihan bukan angka 1, 2, 3, atau 0
    while True:
        pilih = input("> ")
        if pilih == '1':
            beli_obat()
            break
        elif pilih == '2':
            tampil_data('menu')
            break
        elif pilih == '3':
            ke_admin()
            break
        elif pilih == '0':
            exit()
        else:
            print("Perintah salah!")
    
# =================================================
# =================PEMBELIAN OBAT==================
# =================================================
# Menu beli obat
def beli_obat():
    loop = True
    tanya_obat()  # Masuk ke fungsi tanya_obat() untuk membeli
    print()
    
    # Menghitung total harga belanjaan
    total_harga = 0
    for i in range(len(pesanan)):
        harga_dipesan = obat[id_obat[pesanan[i]]]
        banyak_dipesan = kuantitas[i]
        harga_total_dipesan = harga_dipesan * banyak_dipesan
        total_harga += harga_total_dipesan
    print(f"   Total harga: {duit(total_harga)}\n")
    
    # Untuk menginput uang yang akan dibayarkan
    loop = True
    while loop == True:
        try:
            uang_dimiliki = int(input("Berapa banyak uang yang dibayarkan?: Rp"))
            if uang_dimiliki >= total_harga:
                struk(total_harga, uang_dimiliki)
            else:
                while True:
                    # Menanyakan apakah ingin membatalkan pesanan
                    # atau berhutang jika uang kurang
                    print("Uang kurang!\n"
                          "1) Batalkan\n"
                          "2) Hutang")
                    pilih = input("> ")
                    if pilih == '1':
                        loop = False
                        menu_awal()
                        break
                    elif pilih == '2':
                        struk(total_harga, uang_dimiliki)
                        break
                    else:
                        print("Perintah salah!")
        except ValueError:
            print("Bukan format yang benar!")

# Fungsi menunjukkan obat yang dijual beserta harganya
def daftar_obat():
    print()
    print("  DAFTAR OBAT  ".center(45, "="))
    print()
    for i in range(len(obat)):
        # Mencetak daftar obat beserta harganya
        print(f"[{i + 1}] {id_obat[i + 1]}".ljust(30) +
              f"{duit(obat[id_obat[i + 1]])}".rjust(15))
    print()
    print("=" * 45)
    print()

# Fungsi untuk menanyakan apakah ingin membeli, menambahkan,
# menghapus, atau mengonfirmasi item
def tanya_obat():
    loop = True
    while loop == True:
        # Menunjukkan daftar obat
        daftar_obat()
        
        # Menanyakan ingin membeli/menambahkan obat apa.
        while True:
            try:
                dipesan = int(input("Ingin membeli obat apa?: "))
                if dipesan in id_obat.keys():
                    pesanan.append(dipesan)
                    break
            except (ValueError, KeyError):
                print("ID tidak dikenal!")
        
        # Menanyakan kuantitas/banyaknya obat yang dipilih
        while True:
            try:
                dipesan = int(input("Berapa banyak?: "))
                if dipesan > 0:
                    kuantitas.append(dipesan)
                    break
            except (ValueError, TypeError):
                print("Tolong tuliskan angka 1 atau lebih!")
        
        # Menunjukkan daftar belanjaan
        print("\nList belanja:")
        list_belanja()
        
        # Menanyakan ingin menambah, menghapus, atau
        # mengakhiri pembelian
        loop2 = True
        while loop2 == True:
            while True:
                print("Ingin apa lagi?\n"
                      "1) Tambahkan item\n"
                      "2) Hapus item\n"
                      "3) Selesai")
                pilih = input("> ")
                if pilih == '1':
                    loop2 = False
                    break
                elif pilih == '2':
                    if len(pesanan) > 0:
                        hapus_obat()
                        break
                    else:
                        print("Daftar belanja kosong!")
                elif pilih == '3':
                    loop = False
                    loop2 = False
                    break
                else:
                    print("Perintah salah!")

# Fungsi untuk menunjukkan daftar belanja
def list_belanja():
    total_harga = 0
    for i in range(len(pesanan)):
        nama_dipesan = id_obat[pesanan[i]]
        harga_dipesan = obat[id_obat[pesanan[i]]]
        banyak_dipesan = kuantitas[i]
        harga_total_dipesan = harga_dipesan * banyak_dipesan
        print(f"   [{i + 1}]==> {nama_dipesan}:")
        print(f"{duit(harga_dipesan)} × {banyak_dipesan} = {duit(harga_total_dipesan)}\n".rjust(40))
        total_harga += harga_total_dipesan
    print(f"   Total harga: {duit(total_harga)}\n")

# Fungsi untuk menghapus obat pada daftar belanjaan
def hapus_obat():
    # Menunjukkan daftar belanjaan
    list_belanja()
    # Menanyakan yang ingin dihapus
    while True:
        try:
            hapus = int(input("Yang mana yang ingin dihapus?: "))
            if 0 < hapus <= len(pesanan):
                del pesanan[hapus - 1]
                del kuantitas[hapus - 1]
                list_belanja()
                break
        except (ValueError, KeyError):
            print("ID salah!")

# Fungsi untuk konfirmasi struk
def struk(total_harga, uang_dimiliki):
    # Membuat negatif menjadi positif
    kembalian =  abs(uang_dimiliki - total_harga)
    
    print("=" * 40)
    print("  APOTEK GAMAUSAKIT  ".center(40, "="))
    print("  STRUK  ".center(40, "="))
    print("=" * 40)
    list_belanja()
    print(f"   Uang dibayarkan: {duit(uang_dimiliki)}")
    if uang_dimiliki >= total_harga:
        print(f"   Kembalian: {duit(kembalian)}\n")
    else:
        print(f"   Hutang: {duit(kembalian)}\n")
    
    # Konfirmasi
    while True:
        print("1) Konfirmasi\n"
              "2) Batalkan belanjaan")
        pilih = input("> ")
        if pilih == '1':
            cetak_struk(total_harga, uang_dimiliki, kembalian)
            break
        elif pilih == '2':
            menu_awal()
            break
        else:
            print("Input tidak valid!")

# Fungsi untuk mencetak struk
def cetak_struk(total_harga, uang_dimiliki, kembalian):
    print("=" * 40)
    print("  APOTEK GAMAUSAKIT  ".center(40, "="))
    print("  STRUK  ".center(40, "="))
    print(f" {str(dt.datetime.now())[:-7]} ".center(40, "="))
    print("=" * 40)
    list_belanja()
    print(f"   Uang dibayarkan: {duit(uang_dimiliki)}")
    if uang_dimiliki >= total_harga:
        print(f"   Kembalian: {duit(kembalian)}\n")
    else:
        print(f"   Hutang: {duit(kembalian)}\n")
    print("  TERIMA KASIH!  ".center(40, "="))
    
    while True:
        print("\nIngin ekspor struk ke format file .txt?:\n"
              "1) Ya\n"
              "2) Tidak")
        pilih = input("> ")
        if pilih == '1':
            cetak_struk_txt(uang_dimiliki, kembalian)
            break
        elif pilih == '2':
            break
        else:
            print("Perintah tidak valid!")
    
    input("\nTekan 'Enter' untuk melanjutkan...")
    menu_awal()


# Fungsi untuk mencetak struk dengan format file txt
def cetak_struk_txt(uang_dimiliki, kembalian):
    nama_file = str(dt.datetime.now().isoformat(sep='_', timespec='seconds')) + '.txt'
    nama_file = nama_file.replace(':', '.')
    
    os.makedirs('struk', exist_ok=True)
    
    with open('struk\\' + nama_file, 'w') as f:
        f.write("=" * 40 + "\n")
        f.write(" APOTEK GAMAUSAKIT ".center(40, "=") + "\n")
        f.write(" STRUK ".center(40, "=") + "\n")
        f.write(f" {str(dt.datetime.now())[:-7]} ".center(40, "=") + "\n")
        f.write("=" * 40 + "\n")
        f.write("=== Pesanan:\n\n")
        
        total_harga = 0
        for i in range(len(pesanan)):
            nama_dipesan = id_obat[pesanan[i]]
            harga_dipesan = obat[id_obat[pesanan[i]]]
            banyak_dipesan = kuantitas[i]
            harga_total_dipesan = harga_dipesan * banyak_dipesan
            f.write(f"   [{i + 1}]==> {nama_dipesan}:\n")
            f.write(f"{duit(harga_dipesan)} × {banyak_dipesan} = {duit(harga_total_dipesan)}".rjust(40))
            f.write("\n\n")
            total_harga += harga_total_dipesan
        
        f.write(f"   Total harga: {duit(total_harga)}\n")        
        f.write(f"   Uang dibayarkan: {duit(uang_dimiliki)}\n")
        if uang_dimiliki >= total_harga:
            f.write(f"   Kembalian: {duit(kembalian)}\n\n")
        else:
            f.write(f"   Hutang: {duit(kembalian)}\n\n")
            
        f.write(" TERIMA KASIH! ".center(40, "="))
    
    print(f"Struk tersimpan dengan nama {nama_file}")

# Data obat
def tampil_data(menuju):
    daftar_obat()
    input("Tekan 'Enter' untuk melanjutkan...")
    if menuju == 'menu':
        menu_awal()
    elif menuju == 'admin':
        tampilan_admin()

# =================================================
# ======================ADMIN======================
# =================================================

# Masukkan password
def ke_admin():
    password = input("Masukkan password!: ")
    if password == '12':
        tampilan_admin()
    else:
        print("Password salah!\n")
        menu_awal()

# Menu password
def tampilan_admin():
    loop = True
    while loop == True:
        print()
        print("=" * 40)
        print("  MENU ADMIN  ".center(40, "="))
        print("=" * 40)
        print("1) Daftar Data Obat\n"
              "2) Tambah Data Obat\n"
              "3) Sunting Data Obat\n"
              "4) Hapus Data Obat\n"
              "0) Kembali\n")
        print("Pilih perintah!")
        
        while True:
            pilih = input("> ")
            if pilih == '1':
                tampil_data('admin')
                break
            elif pilih == '2':
                tambah_data_obat()
                break
            elif pilih == '3':
                sunting_data_obat()
                break
            elif pilih == '4':
                hapus_data_obat()
                break
            elif pilih == '0':
                menu_awal()
                loop = False
                break
            else:
                print("Perintah salah!")

# Fungsi untuk menambahkan data obat pada database
def tambah_data_obat():
    nama_obat_baru = input("Apa nama obatnya?: ")
    while True:
        try:
            harga_obat_baru = int(input("Berapa harga obatnya?: Rp"))
            break
        except ValueError:
            print("Format tidak valid!")
    
    # Menambah obat baru dan harganya
    global obat
    obat[nama_obat_baru] = harga_obat_baru
    
    # Me-refresh dan menampilkan database
    refresh_dan_daftar_obat()
    
# Fungsi untuk menyunting data obat pada database
def sunting_data_obat():
    daftar_obat()
    while True:
        try:
            input_id_obat = int(input("Apa ID obat yang ingin disunting?: "))
            if input_id_obat in id_obat.keys():
                break
        except ValueError:
            print("Format tidak valid!")
    
    while True:
        print("1) Ganti nama\n"
              "2) Ganti harga")
        while True:
            pilih = input("> ")
            if pilih == '1':
                sunting_nama_obat(input_id_obat)
                break
            elif pilih == '2':
                sunting_harga_obat(input_id_obat)
                break
            else:
                print("Perintah salah!")
        break
    
    # Me-refresh dan menampilkan database
    refresh_dan_daftar_obat()

# Fungsi untuk menyunting nama obat
def sunting_nama_obat(id_):
    # Memanggil variabel global obat dan id_obat
    global obat
    global id_obat
    
    nama_obat_baru = input("Apa nama obatnya?: ")
    
    # Menambah item baru dengan nama berbeda tapi harga sama
    obat[nama_obat_baru] = obat[id_obat[id_]]
    # Menghapus item lama
    obat.pop(id_obat[id_])
    
# Fungsi untuk menyunting harga obat
def sunting_harga_obat(id_):
    # Memanggil variabel global obat dan id_obat
    global obat
    global id_obat
    
    while True:
        try:
            harga_obat_baru = int(input("Berapa harga baru obatnya?: Rp"))
            break
        except ValueError:
            print("Format tidak valid!")

    # Mengganti value/harga barang
    obat[id_obat[id_]] = harga_obat_baru
    

# Fungsi untuk menghapus data obat pada database
def hapus_data_obat():
    # Memanggil variabel global obat dan id_obat
    global obat
    global id_obat
    
    daftar_obat()
    while True:
        try:
            input_id_obat = int(input("Apa ID obat yang ingin dihapus?: "))
            if input_id_obat in id_obat.keys():
                break
        except ValueError:
            print("Format tidak valid!")
    
    # Menghapus obat
    obat.pop(id_obat[input_id_obat])
    
    # Me-refresh dan menampilkan database
    refresh_dan_daftar_obat()

# Me-refresh database sekaligus menampilkan daftar obat
def refresh_dan_daftar_obat():
    refresh_database()
    daftar_obat()
    input("Tekan 'Enter' untuk melanjutkan...")

# Refresh database
refresh_database()

# Membuat menu awal
menu_awal()