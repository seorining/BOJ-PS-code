x = input()
y = input()
z = input()

i = 0
try:
    i = int(x) + 3
except:
    try:
        i = int(y) + 2
    except:
        i = int(z) + 1

if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
elif i % 3 == 0:
    print("Fizz")
elif i % 5 == 0:
    print("Buzz")
else:
    print(i)