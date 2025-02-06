# 연결 요소의 개수 (DFS)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 함수 생성
# 전제: visited[i] = False만 방문
def dfs(graph, v, visited):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# 입력 받기
n, m = map(int, input().split()) 

# 빈 그래프 생성
graph = [[] for _ in range(n+1)]

# 간선의 양 끝점 반복적으로 입력받고 그래프에 추가
for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

# 연결 요소(그래프)의 수
count = 0

# 방문 여부를 표시하기 위해 '빈 그래프' 길이와 동일한 배열 생성
visited = [False] * (n+1)

# dfs 한 번 끝날 때 마다 count += 1
for i in range(1, n+1):
  if not visited[i]:
    dfs(graph, i, visited)
    count += 1

print(count)
