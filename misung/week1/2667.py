import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력 받기
n = int(input().strip())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 방문 여부를 저장하는 배열
visited = [[False] * n for _ in range(n)]


# dfs 함수 생성
def dfs(graph, x, y, visited):
  if x < 0 or x >= n or y < 0 or y >= n:
    return 0
    
  if not visited[x][y] and graph[x][y] == 1:
    visited[x][y] = True
    graph[x][y] = 0  # 방문한 노드를 0으로 처리
    count = 1  # 현재 노드 포함
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      count += dfs(graph, nx, ny, visited)
    return count
  return 0


# 연결된 단지 개수 및 각 단지 크기 저장
result = 0
num = []

for i in range(n):
  for j in range(n):
    if not visited[i][j] and graph[i][j] == 1:
      size = dfs(graph, i, j, visited)
      num.append(size)
      result += 1

num.sort()
print(result)
for i in num:
  print(i)
