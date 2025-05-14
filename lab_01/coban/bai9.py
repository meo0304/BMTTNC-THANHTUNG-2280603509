def kiemtrasonguyento(n):
    if n <=1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i ==0:
            return False
    return True

num=int(input("nhap so can kiem tra: "))
if kiemtrasonguyento(num):
    print(num,"la SNT.")
else:
    print(num,"khong phai SNT.")