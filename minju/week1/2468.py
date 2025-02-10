n = int(input())
graph = []
maxNum = 0
 
 #graph에다가 땅 높이 저장해주기
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j] 
            #maxNum은 가장 높은 땅의 높이이다. 이 높이까지만 강수량을 테스트해주면 된다. 
 
 
 
dx = [0 ,0, 1, -1]
dy = [1, -1, 0 ,0]
def bfs(a, b, value, visited):
    q = []
    q.append((a, b))
    visited[a][b] = 1
 
    while q:
        x, y = q.pop(0)
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
 
 
result = 0
for i in range(maxNum): 
    visited = [[0] * n for i in range(n)]
    cnt = 0
 
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0: 
                bfs(j, k, i, visited)
                cnt += 1
 
    if result < cnt:
        result = cnt
 
print(result)