M,N,K = map(int, input().split())
graph = [[0 for i in range(N)] for j in range(M)]

#모눈종이에 직사각형 색칠해주기
for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            graph[y][x]+=1

#bfs 함수 만들기
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(a,b):
    queue = []
    size = 0
    queue.append((a,b))
    graph[b][a]=1
    while queue:
        x,y = queue.pop(0)
        size+=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<N and 0<=ny<M):    
                if (graph[ny][nx]==0):
                    queue.append((nx, ny))
                    graph[ny][nx]=1
    return size

sizes = []
for i in range(M):
    for j in range(N):
        if (graph[i][j]==0):
            sizes.append(bfs(j,i))

print(len(sizes))
sizes.sort()
for i in sizes:
    print(i, end=" ")
        