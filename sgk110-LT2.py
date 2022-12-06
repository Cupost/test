a = 1
b = 0
while a < 10:
    a =a+3
    if a%5==0:
        b = b+1
    if a%3==1:
        b = b+1
    if a%3==1 and a%5==0:
        b = b-1
print(b)