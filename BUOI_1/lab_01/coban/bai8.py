def chiahetcho5(sonhiphan):

    sothapphan = int(sonhiphan,2)
    if sothapphan % 5 == 0:
        return True
    else:
        return False

chuoisonhiphan = input("nhap chuoi so nhi phan ( phan tach boi dau ',': ")

sonhiphanlist = chuoisonhiphan.split(',')

sochiahetcho5 = [so for so in sonhiphanlist if chiahetcho5 (so)]

if len(sochiahetcho5) > 0:
    kq= ','.join(sochiahetcho5)
    print("cac so nhi phan chia het cho 5 la: ",kq)
else:
    print("Khong co so nhi phan nao chia het cho 5 !!!")
