N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(a,b):
    queue = []
    distance = 1
    queue.append((a,b, distance))
    graph[b][a] = 0
    while queue:
        x,y,d = queue.pop(0)
        d += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx==M-1 and ny==N-1):
                return d
            elif (0<=nx<M and 0<=ny<N and graph[ny][nx]):
                graph[ny][nx]=0
                queue.append((nx, ny, d))
        
print(bfs(0,0))