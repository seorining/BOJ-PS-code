x = int(input())
y = int(input())

a1 = (y%10)*x
a2 = int((y%100)/10)*x
a3 = int(y/100)*x

print(a1)
print(a2)
print(a3)
print(x*y)