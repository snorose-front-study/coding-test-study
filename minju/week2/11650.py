N = int(input())
coord = []
for _ in range(N):
    coord.append(list(map(int, input().split())))

def sortByX(i):
    return i[0]
def sortByY(i):
    return i[1]

coord.sort(key=sortByY)
coord.sort(key=sortByX)

for a,b in coord:
    print(a,b)