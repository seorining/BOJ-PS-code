import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
print_list = []
num_dict = {}
sort_num = sorted(list(set(num_list)))

#(-10, -9, 2, 4)
for i in range(len(sort_num)):
    num_dict[sort_num[i]] = i
#(-10:0, -9:, 1, 2:2, 4:3)

for i in num_list:
    print(num_dict[i], end=' ')