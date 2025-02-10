N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
dfs_graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a] += [b]
    dfs_graph[a] += [b]
    graph[b] += [a]
    dfs_graph[b] += [a]

for _ in range(N+1):
    graph[_].sort()
    dfs_graph[_].sort()

def bfs(v):
    queue = []
    visited = [0]*(N+1)
    queue.append(v)
    visited[v]=1
    while queue:
        x = queue.pop(0)
        print(x,end=" ")
        for i in graph[x]:
            if (visited[i]==0):
                queue.append(i)
                visited[i]=1
        graph[x] = []

def dfs(v,visited):
    print(v, end=" ")
    for i in dfs_graph[v]:
        if (visited[i]==0):
            nv = i
            visited[nv] = 1
            dfs(nv, visited)
            
dfs_visited = [0]*(N+1)
dfs_visited[V] = 1
dfs(V, dfs_visited)
print()
bfs(V)
