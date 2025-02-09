# S2 DFS와 BFS
from collections import deque
import sys

sys.setrecursionlimit(10**6)  # 재귀 탐색 깊이 제한
input = sys.stdin.readline


# DFS 알고리즘
def dfs(x):
    dfs_visited[x] = True
    dfs_order.append(x)

    # 방문 가능한 정점이 여러개인 경우 번호가 작은 것부터 방문
    for i in sorted(graph[x]):
        if not dfs_visited[i]:
            dfs(i)


# BFS 알고리즘
def bfs(x):
    queue = deque([x])
    bfs_visited[x] = True

    while queue:
        node = queue.popleft()
        bfs_order.append(node)

        # 방문 가능한 정점이 여러개인 경우 번호가 작은 것부터 방문
        for i in sorted(graph[node]):
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = True


N, M, V = map(int, input().split())  # 정점의 개수 N, 간선의 개수 M, 탐색 시작 번호 V
graph = [[] for _ in range(N + 1)]
dfs_visited = [False] * (N + 1)  # DFS 알고리즘 용 방문 여부
bfs_visited = [False] * (N + 1)  # BFS 알고리즘 용 방문 여부


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_order = []
bfs_order = []

dfs(V)
bfs(V)

print(*dfs_order)
print(*bfs_order)
