import sys

n = int(sys.stdin.readline().rstrip())

score = [0]
for i in range(n):
    score.append(int(sys.stdin.readline().rstrip()))

dp = [0] * (n+1)

if n == 1:
    dp[1] = score[1]
elif n == 2:
    dp[2] = score[1] + score[2]
else:
    dp[1] = score[1]
    dp[2] = score[1] + score[2]
    dp[3] = score[3] + max(score[1], score[2])

for i in range(4, n+1):
    dp[i] = score[i] + max(dp[i-2], score[i-1]+dp[i-3])

print(dp[n])