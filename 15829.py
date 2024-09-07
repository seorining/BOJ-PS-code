from string import ascii_lowercase

alphabetDict = {}

i = 1
for _ in ascii_lowercase:
    alphabetDict[_] = i
    i += 1

# for key, value in alphabetDict.items():
#     print(f"{key} : {value}  ")

input()
string = list(input())

hashNum = 0
i = 0

for _ in string:
    hashNum += alphabetDict[_] * (31 ** i)
    i += 1

print(hashNum % 1234567891)