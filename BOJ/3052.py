num = [int(input()) for _ in range(10)]

remain = []

for _ in num:
    remain.append(_ % 42)

print(len(set(remain)))