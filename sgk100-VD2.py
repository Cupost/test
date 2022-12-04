import math 
# Khai báo thư viện 

a = int(input())
b = int(input())
c = int(input())
# Nhập số từ bàn phím 

d = a+b+c
p = d/2
e = p*(p-a)*(p-b)*(p-c)
# Quy đổi bằng công thức toán học

print(math.sqrt(e))
print(d)
# In ra màn hình 

