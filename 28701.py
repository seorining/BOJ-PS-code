n = int(input())

sum = 0
sum_triple = 0
for i in range(1, n+1):
    sum += i
    sum_triple += i * i * i
    
sum_squre = sum * sum

print(sum)
print(sum_squre)
print(sum_triple)
