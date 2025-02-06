import sys

input = sys.stdin.readline

n = int(input()) # 컴퓨터의 개수
v = int(input()) # 연결되어 있는 컴퓨터 쌍의 수 = 연결선의 개수
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = -1

for _ in range(v):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def DFS(v):
  visited[v] = True
  global count
  count += 1
  for i in graph[v]:
    if not visited[i]:
      DFS(i)

DFS(1)
print(count)