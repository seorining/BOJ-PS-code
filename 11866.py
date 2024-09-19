n, k = map(int, input().split())

sitList = [i+1 for i in range(n)]
outList = []

index = k-1

for _ in range(n):
    if len(sitList) == 1:
        outList.append(sitList.pop())
        break
    outList.append(sitList.pop(index))
    
    index += k-1
    index = index % (len(sitList))

print("<", end='')
for i in range(n-1):
    print(f"{outList[i]}, ", end='')
print(f"{outList[-1]}>")