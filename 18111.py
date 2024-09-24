import math
import sys
input = sys.stdin.readline

n, m, my_block = map(int, input().split())
ground = []
for _ in range(n):
    ground.extend(map(int, input().split()))

ground_height = 0
taken_time = math.inf
min_height = min(ground)
max_height = max(ground) + (my_block // n*m)

for height in range(min_height, max_height+1):
    dig_block = 0
    used_block = 0
    
    for corr_height in ground:
        if corr_height > height:
            dig_block += corr_height - height
        else:
            used_block += height - corr_height
            
    if dig_block + my_block < used_block:
        break
    
    used_time = dig_block * 2 + used_block
    
    if used_time <= taken_time:
        taken_time = used_time
        ground_height = height


print(taken_time, ground_height)