N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
connected_comp_num = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u]+=[v]
    graph[v]+=[u]
    
for a in range(N):
    if visited[a+1] == 0:
        queue = [a+1]
        visited[a+1] = 1
        while queue:
            n = queue.pop(0)
            for i in graph[n]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1
        connected_comp_num += 1

print(connected_comp_num)
