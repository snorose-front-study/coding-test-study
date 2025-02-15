number = input()
number_list = number.split("-")
count = 0

for num in number_list:
    if (count==0):
        result = sum(list(map(int, num.split("+"))))
    else:
        result -= sum(list(map(int, num.split("+"))))
    count += 1

print(result)