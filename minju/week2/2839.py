weight = int(input())
repeat = weight//5

def sugar_factory():
    for i in range(repeat,-1,-1):
        if ((weight-i*5)%3==0):
            return i+(weight-i*5)//3
    return -1

print(sugar_factory())
