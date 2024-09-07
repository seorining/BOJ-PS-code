n = int(input())

strList = list(set([input() for _ in range(n)]))
strList.sort()
strList.sort(key=len)

print(*strList, sep='\n')