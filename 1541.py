expression = input()
num_list = expression.split("-")
sum_num = sum(map(int, num_list[0].split("+")))

for i in num_list[1:]:
    sum_num -= sum(map(int, i.split("+")))
    
print(sum_num)