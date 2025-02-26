N, C = map(int, input().split())
num_list = list(map(int, input().split()))
rearrange_num_dic = {}

for i in num_list:
    if i not in rearrange_num_dic.keys():
        rearrange_num_dic[i] = 1
    else:
        rearrange_num_dic[i] += 1

rearrange_num_dic = {k:v for k,v in sorted(rearrange_num_dic.items(), key=lambda item:item[1], reverse=True)}
for k, v in rearrange_num_dic.items():
    for _ in range(v):
        print(k, end=" ")