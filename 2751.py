import sys
numList = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
print(*sorted(list(set(numList))), sep='\n')