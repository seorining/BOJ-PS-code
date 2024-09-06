L = int(input())

t = L // 5
L = L % 5
t += L // 4
L = L % 4
t += L // 3
L = L % 3
t += L // 2
L = L % 2
t += L // 1
print(t)