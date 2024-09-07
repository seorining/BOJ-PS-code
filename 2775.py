resident = []
apartment = [[i+1 for i in range(14)]]
kList = []
tList = []

testcase = int(input())

for _ in range(testcase):
    k = int(input())
    t = int(input())
    kList.append(k)
    tList.append(t)

maxK = max(kList)
maxT = max(tList)

for i in range(1, maxK+1):
    line = []
    sum = 0
    for j in range(maxT):
        sum += apartment[i-1][j]
        line.append(sum)
    apartment.append(line)
for _ in range(testcase):
    print(apartment[kList[_]][tList[_]-1])
