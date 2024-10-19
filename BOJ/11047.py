n, k = map(int, input().split())

coin_list = []

for i in range(n):
    coin_list.append(int(input()))

count = 0

while True:
    if k == 0:
        break
    
    find_coin = 0
    for i in coin_list:
        if i > k:
            break
        find_coin = i
    
    count += k // find_coin
    k = k % find_coin
    
print(count)