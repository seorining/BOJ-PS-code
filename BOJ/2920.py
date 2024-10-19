code = list(map(int, input().split()))

search = [i for i in range(1, 9)]

if code == search:
    print('ascending')
elif code == list(reversed(search)):
    print('descending')
else:
    print('mixed')