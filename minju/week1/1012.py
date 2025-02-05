from collections import deque
T = int(input())

def find_num_of_bug(M,N):
    garden = []
    bug_num = 0

    for i in range(K):
        garden.append(list(map(int, input().split())))

    while garden:
        Q=deque([garden[0]])
        garden.pop(0)
        while Q:
            x,y = Q.popleft()
            if x>0 and [x-1,y] in garden:
                garden.remove([x-1, y])
                Q.append([x-1, y])
            if x<M-1 and [x+1,y] in garden:
                garden.remove([x+1, y])
                Q.append([x+1, y])
            if y>0 and [x,y-1] in garden:
                garden.remove([x, y-1])
                Q.append([x, y-1])
            if y<N-1 and [x,y+1] in garden:
                garden.remove([x, y+1])
                Q.append([x, y+1])
        bug_num+=1
    print(bug_num)

for j in range(T):
    M, N, K = map(int, input().split())
    find_num_of_bug(M,N)