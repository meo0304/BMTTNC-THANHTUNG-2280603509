def taotupletulist(lst):
    return tuple(lst)

input_list = input("nhap ds cac so, cach nhau bang dau ',': ")
numbers = list(map(int, input_list.split(',')))

my_tuple = taotupletulist(numbers)
print("List: ",numbers)
print("Tuple tu List: ",my_tuple)