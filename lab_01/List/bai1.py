def tintongsochan(lst):
    tong=0
    for num in lst:
        if num % 2 == 0:
            tong+= num
    return tong

input_list = input("nhap ds cac so, cach nhau bang dau ',': ")
numbers = list(map(int, input_list.split(',')))

tongchan = tintongsochan(numbers)
print("tong cac so chan trong list: ",tongchan)
