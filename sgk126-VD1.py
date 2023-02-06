s=input("Nhập hai số tự nhiên cách nhau bởi dấu cách: ")

A=s.split(" ")

a=int(A[0])

b=int(A[1])

r = a % b

while r != 0:

    a = b

    b = r

    r = a % b
print(A)
print(s)

print("ƯCLN của a và b là: ",b) 
