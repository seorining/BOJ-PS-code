submit = []
for i in range(28):
    submit.append(int(input()))
    
submit.sort()

for i in range(1,31):
    if i not in submit:
        print(i)