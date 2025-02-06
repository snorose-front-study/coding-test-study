# S3 바이러스


# DFS 알고리즘
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


N = int(input())  # 총 컴퓨터의 수
m = int(input())  # 컴퓨터 쌍의 수
graph = [[] for _ in range(N + 1)]  # 연결 그래프
visited = [0] * (N + 1)  # 방문 여부
cnt = 0  # 감염 컴퓨터 수

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(cnt)
