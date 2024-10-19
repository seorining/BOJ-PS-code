op = list(input())
num_list = []

for i in op:
    if (i.isdigit()):
        num_list.append(int(i))
        
if num_list[0] + num_list[1] == num_list[2]:
    print("YES")
else:
    print("NO")