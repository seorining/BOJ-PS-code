import sys

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())
    clothes_dict = {}
    sum_combination = 1
    for _ in range(m):
        clothes, types = sys.stdin.readline().rstrip().split()
        if types in clothes_dict:
            clothes_dict[types].append(clothes)
        else:
            clothes_dict[types] = [clothes]
            
    for i in clothes_dict.values():
        count = len(i) + 1
        sum_combination *= count
        
    print(sum_combination - 1)