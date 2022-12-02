import math 
a = int(input())
b = int(input())
c = int(input())
d = a+b+c
p = d/2
e = p*(p-a)*(p-b)*(p-c)
print(math.sqrt(e))
print(d)

