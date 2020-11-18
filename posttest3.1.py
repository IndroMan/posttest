varian1 = 45
varian2 = 40
def v1():
    while(True):
        jumlah1 = int(input("Mau beli berapa porsi ? "))
        if (jumlah1 > varian1):
            print("Out Of Stock\n")
            break
        elif (jumlah1 >= 10):
            print("SELAMET ANDA KENA DISKON SEBESAR 10%")
            total_harga = jumlah1 * 2000
            print("Harga awal anda : ", total_harga)
            diskon1 = 10/100 * total_harga
            print("Harga Setelah Diskon : ", diskon1)
            print("Terimakasih telah berbelanja silahkan datang kembali!")
            sstok = varian1 - jumlah1
            print("Sisa Stock Takoyaki Old : ", sstok)
            print("\n")
            break
        else:
            print("Total Harga Anda sebesar : ", total_harga)
            print("Terimakasih telah berbelanja silahkan datang kembali!")
            sstok = varian1 - jumlah1
            print("Sisa Stock Takoyaki Old : ", sstok)
            print("\n")
            break    

def v2():
    while(True):
        jumlah2 = int(input("Mau beli berapa pcs? : "))
        if(jumlah2>varian2):
        print("Out Of Stock\n")
        break
        elif (jumlah2 >= 8):
            print("SELAMET ANDA KENA DISKON SEBESAR 10%")
            total_harga = jumlah2 * 2500
            print("Harga awal anda : ", total_harga)
            diskon2 = 8/100 * total_harga
            print("Harga Setelah Diskon : ", diskon2)
            print("Terimakasih telah berbelanja silahkan datang kembali!")
            print("\n")
            break
        else:
            print("Total Harga Anda sebesar : ", total_harga)
            print("Terimakasih telah berbelanja silahkan datang kembali!")
            print("\n")
            break
def menu():
    print("SELAMAT DATANG DI WELLCOMEYAKI")
    print("1. Takoyaki Old = Rp.2000/pcs")
    print("2. Takoyaki All New = Rp.2500/pcs")
    print("ADA PROMO SPESIAL GAESSS!!")
    print("TAKOYAKI OLD BELI 10 ATAU LEBIH DAPAT DISKON 10%")
    print("TAKOYAKI ALL NEW BELI 8 ATAU LEBIH DAPAT DISKON 8%")

    print("Inputkan angka 1/2 untuk memesan")
    pilih = input("Mau beli yang mana ? ")
    
    if pilih == "1":
        v1()
    elif pilih == "2":
        v2()
    else:
        print("Inputkan Angka 1/2!!!")
        print("\n")

if __name__ == "__main__":
    while(True):
        menu()