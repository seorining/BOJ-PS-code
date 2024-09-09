from collections import deque

n = int(input())

for _ in range(n):
    printer = deque()
    docNum, ask = map(int, input().split())
    priority =list(map(int, input().split()))
    
    for i in range(docNum):
        printer.append([i, priority[i]])
    
    count = 0
    while True:
        first = max(printer, key=lambda x: x[1])[1]
        
        if printer[0][1] == first:
            count += 1
            if printer[0][0] == ask:
                print(count)
                break
            else:
                printer.popleft()
        else:
            printer.append(printer.popleft())