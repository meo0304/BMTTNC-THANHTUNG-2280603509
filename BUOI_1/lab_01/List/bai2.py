def daonguoclist(lst):
    return lst[::-1]

input_list = input("nhap ds cac so, cach nhau bang dau ',': ")
numbers = list(map(int, input_list.split(',')))

listdaonguoc = daonguoclist(numbers)
print("List sau khi dao nguoc: ",listdaonguoc)




