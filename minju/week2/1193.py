number = int(input())
marker = 1
adder = 1
row = 1

while True:
    adder += 1
    if (marker >= number):
        break
    row += 1
    marker += adder
place = number - (marker-(adder-1))

s = row+1
if (row%2==0):
    print(place,"/",s-place, sep="")
else:
    print(s-place, "/", place, sep="")

