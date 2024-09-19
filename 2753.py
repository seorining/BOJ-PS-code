year = int(input())

Isleap = False

if year % 4 == 0 :
    Isleap = True
    if year % 100 == 0:
        Isleap = False
    if year % 400 == 0:
        Isleap = True

if Isleap:
    print("1")
else:
    print("0")