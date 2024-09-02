x, y = map(int, input().split())

absoluteValue = x - y
if absoluteValue < 0:
    absoluteValue = -absoluteValue

print(absoluteValue)