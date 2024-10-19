import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
noListenPeople = set()
noSeePeople = set()

for i in range(n):
    noListenPeople.add(sys.stdin.readline().rstrip())

for i in range(m):
    noSeePeople.add(sys.stdin.readline().rstrip())
    # noSeePeople.append(sys.stdin.readline().rstrip())

noListenSeePeople = list(noListenPeople & noSeePeople)
noListenSeePeople.sort()

print(len(noListenSeePeople))
print(*noListenSeePeople, sep='\n')