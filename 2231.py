N = int(input())

check=False
try :
    for i in range(N - 9*len(str(N)), N+1):
        string = list(str(i))
        sum = i
        for j in string:
            sum += int(j)
            
        if sum == N:
            print(i)
            check = True
            break
except:
    for i in range(1, N+1):
        string = list(str(i))
        sum = i
        for j in string:
            sum += int(j)
            
        if sum == N:
            print(i)
            check = True
            break

if not check:
    print(0)