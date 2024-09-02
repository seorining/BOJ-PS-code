hour, minute = map(int, input().split())

if minute < 45 :
    hour -= 1
    minute = minute + 60 - 45
else :
    minute -= 45
    

if hour <0:
    hour = 23
    
print(f"{hour} {minute}")