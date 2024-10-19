import sys
input = sys.stdin.readline

n = int(input())

numList = []
for i in range(n):
    numList.append(int(input()))

def findMean():
    summation = 0
    for i in numList:
        summation += i
    return (summation + len(numList)//2) // len(numList)

def mean():
    numList.sort()
    mid = len(numList) // 2
    return numList[mid]

def mode():
    modeDic = {}
    for i in numList:
        if i in modeDic:
            modeDic[i] += 1
        else:
            modeDic[i] = 1
            
    manyNum = max(modeDic.values())  
    manyList = []
    for i in modeDic.keys():
        if manyNum == modeDic[i]:
            manyList.append(i)
            
    return manyList[1] if len(manyList) > 1 else manyList[0]
    
def rangeList():
    return max(numList) - min(numList)

print(findMean())
print(mean())
print(mode())
print(rangeList())