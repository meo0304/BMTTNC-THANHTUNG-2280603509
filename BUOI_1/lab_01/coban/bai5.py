sogiolam = float(input("nhap so gio lam moi tuan: "))
luonggio = float(input("nhap so luong/gio: "))
giotieuchuan = 44
giovuotchuan = max(0,sogiolam - giotieuchuan)
tienluong = giotieuchuan * luonggio + giovuotchuan * luonggio * 1.5
print (f"tien luong: {tienluong}")
