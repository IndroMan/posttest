obat = []

def show_data():
    if len(obat) <= 0:
        print ("BELUM ADA DATA")
    else:
        print("Semua obat ada {}".format(len(obat)))
        print(obat)


def insert_data():
    obat_baru = input("Nama Obat: ")
    obat.append(obat_baru)

# fungsi untuk edit data
def edit_data():
    show_data()
    indeks = input("Inputkan Nama obat: ")
    if(indeks == (obat)):
        print ("Nama salah")
    else:
        nama_baru = input("Nama baru: ")
        for i, item in enumerate(obat):
            if item==indeks:
                obat[i]=nama_baru

# fungsi untuk menhapus data
def delete_data():
    show_data()
    indeks = input("Inputkan Nama obat: ")
    if(indeks == (obat)):
        print ("Nama salah")
    else:
        obat.remove(indeks)

def beli_obat():
    show_data()
    nama = input("Masukkan Nama Pembeli : ")
    indeks = input("Nama Obat yang dibeli : ")
    harga = int(input("Masukkan Harga Obat : "))
    jumlah = int(input("Berapa kepeng/botol : "))
    uang = int(input("Uang Tunai: Rp."))
    total_harga = harga*jumlah
    print("=========================")
    print("======= S T R U K =======")
    print("=========================")
    print ("=== Nama      :",nama)
    print ("=== Tagihan   :Rp.",total_harga)
    print ("=== Beli      :",indeks)
    print ("=== Uang      :Rp.",uang)
    akhir=int(uang-total_harga)
    print ("=== Kembalian :Rp.",akhir)
    print("=========================")
    print("=========================")




# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU ----------")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Beli Obat")
    print ("[6] Exit")
    
    menu = input("PILIH MENU> ")
    print ("\n")

    if menu == "1":
        show_data()
    elif menu == "2":
        insert_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        beli_obat()
    elif menu == "6":
        exit
    else:
        print ("Salah pilih!")

if __name__ == "__main__":

    while(True):
        show_menu()
print("=========================")
print("======= S T R U K =======")
print("=========================")
print ("=== Nama      :",nama)
print ("=== Beli      :",indeks)
print ("=== Tagihan   :Rp.",total_harga)
print ("=== Uang      :Rp.",uang)
print ("=== Kembalian :Rp.",akhir)
print("=========================")
print("=========================")