from operator import index

import numpy
from numpy import random
from numpy.f2py.crackfortran import word_pattern

#1. Viết chương trình tính tổng 5 số được nhập vào từ bàn phím.

# x = random.randint(100, size=(5))
# print(x)
# sum = 0;
# for i in x:
#     sum += i
#
# print(sum)


#2 Viết chương trình tính tổng n số được nhập vào từ bàn phím, kết thúc bằng
#phím ‘e’ hoặc ‘E’.

# sum=0
# n= int(input("enter number: "))
# while (n!='e' or n!= 'E' ):
#     sum += int(n)
#     n = input("enter number: ")
#
#
# print(sum)

# 3. Viết chương trình tính tổng các số chẳn dương được nhập vào từ bàn phím.
# Khi chạy chương trình: xuất ra các số vừa nhập vào, và kết quả.
# input = input("Enter elements separated by space: ").split()
# sum=0
# for i in input:
#     sum+=int(i)
# print("List:", input)
# print(sum)

# 4. Viết chương trình tính tổng các số từ 1 đến n. n được nhập vào từ bàn phím
# n = int(input("Nhap so luong phan tu: "))
# sum=0
# i=1
# while(i<=n):
#     sum+=i
#     i=i+1
#
# print(sum)

# 5. Viết chương trình tìm số lớn nhất, nhỏ nhất từ 3 số được nhập vào từ bàn
# phím.
# arr= list(map(int, input("Nhap cac phan tu: ").split()))
#
# print ("Min: ", numpy.min(arr))
# print ("Max: ",numpy.max(arr))

 # 6. Cho danh sách như sau ds = [5, 2, 10, 32, 11, 48, 34]. Tính tổng các giá trị tại vị
# trí chẵn nếu giá trị đó là chẵn.

# ds = [5, 2, 10, 32, 11, 48, 34]
# sum=0
#
# for i in range(len(ds)):
#     if(i%2==0):
#         if(ds[i]%2==0):
#             print(i ," ")
#             sum+=ds[i]
#
# print(sum)

#7. Cho danh sách như sau ds = [15, 32, 10, 32, 29, 48, 15]. Viết chương trình xóa
#các giá trị lẻ trong danh sách.
# ds = [15, 32, 10, 32, 29, 48, 15]
#
# for i in ds:
#     if int(i) % 2 != 0:
#          ds.remove(i)
#
# print(ds)

#8. Viết hàm đếm số ký tự, số chữ của một câu được nhập vào từ bàn phím.
# def count_char():
#     input_text=input("nhap cau: ")
#     text= input_text.split(" ")
#     text_count=len(text)
#     print("so chu: ",text_count)
#     print("so ki tu", len(input_text))
#
# count_char()

#9. Viết chương trình đếm số chữ tìm được trong một đoạn văn.
# Ví dụ: Tìm chữ ‘Python’ có trong đoạn văn nào đó, và hiển thị số lần xuất hiện
# của chữ Python.
# input_text=input("nhap cau: ")
# text_count = input_text.count("Python")
# print("so chu Python: ",text_count)

#10. .Viết chương trình thay thế chuỗi trong một đoạn văn (không sử dụng hàm
# replace có sẵn)
# Ví dụ: Tìm tất cả các chữ ‘data’ có trong đoạn văn và thay thế bằng chữ ‘dữ
# liệu’. Sau đó xuất ra chuỗi mới sau khi đã thay thế.

# input_text=input("nhap cau: ")
# new_text= input_text.replace("data", "du lieu")
#
# print(new_text)

#11. Viết chương trình đọc số. Người dùng nhập vào 1 số, chương trình đọc số vừa
#nhập vào. Ví dụ số 321 -> Chương trình xuất ra câu: Ba trăm hai mươi mốt
# text_convert="";
# input_text=input("nhap so: ")
# text_split= list(input_text)
# print(text_split)
# convert_num= {0:'khong',1:'mot', 2:'hai', 3:'ba', 4:'bon', 5:'nam', 6:'sau', 7:'bay', 8:'tam', 9:'chin'}
# donVi=['chuc','tram','nghin','trieu']
# for i in range(len(text_split)):
#     digit = int(text_split[i])  # Convert string to integer to look up the correct word
#     if digit == 0:
#         text_convert += convert_num[digit]  # "không" for zero
#     else:
#         text_convert += convert_num[digit]  # Add the Vietnamese word for the number
#
#     # Handle placing the correct unit (e.g., chục, trăm, nghìn) if it's not the last digit
#     if length - i - 1 == 1:
#         text_convert += " " + donVi[0]  # Add "chục" after the second-to-last digit
#     elif length - i - 1 == 2:
#         text_convert += " " + donVi[1]  # Add "trăm" after the third-to-last digit
#     elif length - i - 1 == 3:
#         text_convert += " " + donVi[2]  #
#
# print(" Nhap chu: ")
