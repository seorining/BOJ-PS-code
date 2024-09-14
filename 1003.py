n = int(input())

dp_table = [[0,0] for _ in range(41)]
dp_table[0] = [1,0]
dp_table[1] = [0,1]

idx = 1
for _ in range(n):
    num = int(input())
    if num > idx:
        for i in range(idx+1,num+1):
            for j in range(2):
                dp_table[i][j] = dp_table[i-1][j] + dp_table[i-2][j]
        idx = num
        print(dp_table[num][0], dp_table[num][1])
    else:
        print(dp_table[num][0], dp_table[num][1])