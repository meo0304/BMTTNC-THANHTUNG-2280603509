def demsolanxuathien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] +=1
        else:
            count_dict[item] =1
    return count_dict

input_string = input("nhap danh sach cac tu, cach nhau bang dau cach (nhap xong bam dau ','): ")
word_list = input_string.split()

solanxuathien = demsolanxuathien(word_list)
print("so lan xuat hien cac phan tu: ",solanxuathien)
