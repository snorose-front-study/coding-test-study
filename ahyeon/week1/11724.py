# S2 연결 요소의 개수
import sys

sys.setrecursionlimit(10**6)  # 런타임에러 해결용 리밋설정


# DFS 알고리즘
def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


N, M = map(int, sys.stdin.readline().split())  # 정점의 개수 N, 간선의 개수 M
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())  # 간선의 양 끝점
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)  # 방문 여부
cnt = 0  # 연결 요소의 개수

for i in range(1, N + 1):
    if not visited[i]:
        if not graph[i]:  # 그래프가 연결되지 않은 경우 바로 cnt 증가
            cnt += 1
            visited[i] = 1
        else:  # 연결된 그래프가 있는 경우 dfs알고리즘 탐색으로 visited 여부 체크 후 cnt 증가
            dfs(i)
            cnt += 1

print(cnt)
