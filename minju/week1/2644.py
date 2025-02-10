n = int(input())
h1, h2 = list(map(int, input().split()))
m = int(input())

humans = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    humans[a]+=[b]
    humans[b]+=[a]

queue = []
queue.append((h1,0))

while (queue):
    h, chonsu = queue.pop(0)
    if h==h2:
        print(chonsu)
        queue.append(True)
        break
    chonsu += 1
    for i in humans[h]:
        queue.append((i,chonsu))
    humans[h] = []

if not queue:
    print(-1)