not_self_number_list = []

for i in range(10000):
    not_self_number = i
    num = str(i)
    for j in num:
        not_self_number += int(j)
    if (not_self_number>10000):
        continue
    not_self_number_list.append(not_self_number)

set(not_self_number_list)
not_self_number_list.sort()

for i in range(10000):
    if i not in not_self_number_list:
        print(i)