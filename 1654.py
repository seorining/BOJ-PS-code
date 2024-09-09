import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lanLine = []
for i in range(k):
    lanLine.append(int(input()))
    
    
start = 1
end = max(lanLine)
line = (start + end) // 2

while start <= end:
    mid = (start + end) // 2
    
    count = 0
    for i in lanLine:
        count += i // mid
    
    if count >= n:
        line = mid
        start = mid + 1
    else :
        end = mid - 1
        
print(line)