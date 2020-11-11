a=str(input("Tentukan suhu yang ingin di konversi ? Pilih C/R/F/K : "))
if (a == "C"):
    C=float(input("Masukkan Nilai Suhu Celcius yang ingin kamu konversi : "))
    Ca=str(input("Ingin mengkonversi ke satuan apa ? pilih R/F/K : "))
    if (Ca == "R"):
        RC=((4/5)*C)
        print("Jadi, Suhu celcius bila di konversi menjadi Reamur adalah : ", RC)
    if (Ca == "F"):
        FC=(((9/5)*C)+32)
        print("Jadi, Suhu celcius bila di konversi menjadi Farenheit adalah : ", FC)
    if (Ca == "K"):
        KC=(273+C)
        print("Jadi, Suhu celcius bila di konversi menjadi Kelvin adalah : ", KC)
    
elif (a == "R"):
    R=float(input("Masukkan Nilai Suhu Reamur yang ingin kamu konversi : "))
    Ra=str(input("Ingin mengkonversi ke satuan apa ? pilih C/F/K : "))
    if (Ra == "C"):
        CR=((5/4)*R)
        print("Jadi, Suhu Reamur bila di konversi menjadi Celcius adalah : ", CR)
    if (Ra == "F"):
        FR=(((9/4)*R)+32)
        print("Jadi, Suhu Reamur bila di konversi menjadi Farenheit adalah : ", FR)
    if (Ra == "K"):
        KR=(((5/4)*R)+273)
        print("Jadi, Suhu Reamur bila di konversi menjadi Kelvin adalah : ", KR)
elif (a == "F"):
    F=float(input("Masukkan Nilai Suhu Farenheit yang ingin kamu konversi"))
    Fa=str(input("Ingin mengkonversi ke satuan apa ? pilih C/R/K : "))
    if(Fa == "C"):
        CF=((F-32)*(5/9))
        print("Jadi, Suhu Farenheit bila di konversi menjadi Celcius adalah : ", CF)
    if(Fa == "R"):
        RF=(((4/9)*(F-32)))
        print("Jadi, Suhu Farenheit bila di konversi menjadi Reamur adalah : ", RF)
    if(Fa == "K"):
        KF=(((x-32)*(5/9))+273)
        print("Jadi, Suhu Farenheit bila di konversi menjadi Kelvin adalah : ", KF)
elif (a == "K"):
    K=float(input("Masukkan Nilai Suhu Kelvin yang ingin kamu konversi : "))
    Ka=str(input("Ingin Mengkonversi ke satuan apa ? pilih C/R/F : "))
    if(Ka == "C"):
        CK=(K-273)
        print("Jadi, Suhu Kelvin bila di konversi menjadi celcius adalah : ", CK)
    if(Ka == "R"):
        RK=((K-273)*(4/5))
        print("Jadi, Suhu Kelvin bila di konversi menjadi Reamur adalah : ", RK)
    if(Ka == "F"):
        FK=(((K-273)*(9/5))+32)
        print("Jadi, Suhu Kelvin bila di konversi menjadi Farenheit adalah : ", FK)


