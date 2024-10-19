word = input()
out = [-1]*26

for index, value in enumerate(word):
    if out[ord(value) - 97] == -1:
        out[ord(value) - 97] = index

print(*out, sep=' ')