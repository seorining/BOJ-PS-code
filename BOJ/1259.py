string = []

while True:
    inputString = input()
    if inputString == '0': break
    else : string.append(inputString)

for case in string:
    check = True
    case = list(case)
    length = len(case)
    
    if length % 2 != 0:
        case.pop(length // 2)
        length -= 1
        
    for i in case:
        if i != case[length-1]:
            check = False
        length -= 1

    print("yes") if check else print("no")