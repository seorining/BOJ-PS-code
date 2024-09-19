n = int(input())

for i in range(2*n-1):
    if i == 0 or i == 2*n-2:
        print(*(['*' for _ in range(n)] + [' ' for _ in range(2*n-3)] + ['*' for _ in range(n)]), sep='')
    elif i == n-1:
        print(*([' ' for _ in range(n-1)] + ['*'] + [' ' for _ in range(n-2)] + ['*'] + [' ' for _ in range(n-2)] + ['*']), sep ='')
    else:
        if i < n-1:
            print(*([' ' for _ in range(i)] + ['*'] + [' ' for _ in range(n-2)] + ['*'] + [' ' for _ in range(2*(n-i)-3)] + ['*'] + [' ' for _ in range(n-2)] + ['*']), sep='')
        else:
            i = i - n
            print(*([' ' for _ in range(n-i-2)] + ['*'] + [' ' for _ in range(n-2)] + ['*'] + [' ' for _ in range(2*i+1)] + ['*'] + [' ' for _ in range(n-2)] + ['*']), sep='')