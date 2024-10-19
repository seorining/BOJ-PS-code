def fac(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

n, k = map(int, input().split())
print(fac(n) // (fac(k)*fac(n-k)))