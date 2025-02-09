N = int(input())
graph = [[] for i in range(N+1)]
visited = [0]*(N+1)

for i in range(N-1):
    a,b = map(int, input().split())
    graph[a]+=[b]
    graph[b]+=[a]

def bfs(a):
    queue = []
    parents = []
    queue.append(a)
    visited[a] = 1
    while queue:
        u = queue.pop(0)
        for i in graph[u]:
            queue.append(i)
            #i는 노드 이름, u는 그 노드의 부모
            if (visited[i]==0):
                parents.append((i,u))
            visited[i]=1
        graph[u] = []
    return parents

def sortFun(i):
    a,b = i
    return a

result = bfs(1)
result.sort(key=sortFun)
for a,b in result:
    print(b)