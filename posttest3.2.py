x = 0
N = int(input("Masukkan Nilai N : "))
while(x < N):
    if(10 ** x > N):
        break
    else:
        print("Hasil Perulangannya adalah :")
    x +=1
    print("Nilai terkecil 10^x yang lebih dari N", 10 ** x)
