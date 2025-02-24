M, N = map(int, input().split())
prime = []

def check_prime(num):
    if (num==2 or num==3):
        return True
    for i in prime:
        if (i>num**(1/2)):
            break
        if (num%i==0):
            return False
    return True

for i in range(2,N+1):
    if (check_prime(i)):
        prime.append(i)
        if (i>=M):
            print(i)
