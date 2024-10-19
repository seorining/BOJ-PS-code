n = int(input())
peopleList = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    peopleList.append([age, name])

peopleList.sort(key = lambda x: x[0])

for age, name in peopleList:
    print(f"{age} {name}")
    