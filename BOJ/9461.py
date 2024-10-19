m_list = []

for _ in range(int(input())):
    m_list.append(int(input()))

max_num = max(m_list) + 1
dp = [1] * max_num

for i in range(4, max_num):
    dp[i] = dp[i-2] + dp[i-3]
    
for i in m_list:
    print(dp[i])