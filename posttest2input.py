print("Ini Helm")

helm = []

nm_helm = input("Masukkan Merk Helm : ")
helm.append(nm_helm)

thn_helm = int(input("Tahun Berapa Keluar nya : "))
helm.append(thn_helm)

diameter_helm = float(input("Diameter besar Helm : "))
helm.append(diameter_helm)

uk_helm = input("Ukuran Helm : ")
helm.append(uk_helm)

warna_helm = input("Warna Helm : ")
helm.append(warna_helm)

print("Merk helm adalah", nm_helm, thn_helm,"Diameter Kepala helm adalah", diameter_helm,
        "Kategori Ukuran Helm adalah", uk_helm,"Dan Warna Helm adalah", warna_helm)

print(helm)