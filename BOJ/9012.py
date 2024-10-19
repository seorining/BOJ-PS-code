from collections import deque

sentence = []
T = int(input())
for i in range(T):
    temp = input()
    sentence.append(temp)
    
for i in sentence:
    tempList = deque(i)
    check = True
    stack = deque([0,0])
    while len(tempList) > 0:
        char = tempList.popleft()
        if char == '(':
            stack.append('(')
        elif char == ')':
            out = stack.pop()
            if out != '(':
                check = False
                break
        else:
            continue
    if stack.pop() != 0: check = False
    print("YES") if check else print("NO")