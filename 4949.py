from collections import deque

sentence = []
while True:
    temp = input()
    if temp == '.':
        break
    sentence.append(temp)
    
    
for i in sentence:
    tempList = deque(i)
    check = True
    stack = deque([0,0])
    while len(tempList) > 0:
        char = tempList.popleft()
        if char == '(':
            stack.append('(')
        elif char == '[':
            stack.append('[')
        elif char == ')':
            out = stack.pop()
            if out != '(':
                check = False
                break
        elif char == ']':
            out = stack.pop()
            if out != '[':
                check = False
                break
        else:
            continue
    if stack.pop() != 0: check = False
    print("yes") if check else print("no")