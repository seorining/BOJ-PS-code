answer = []

while True:
    A = list(map(int, input().split()))
    if A[0] == 0:
        break
    A.sort()
    if A[0]*A[0] + A[1]*A[1] == A[2]*A[2]:
        answer.append("right")
    else:
        answer.append("wrong")
        
print(*answer, sep='\n')