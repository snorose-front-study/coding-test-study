# 섬의 개수

# 무한 재귀호출 방지
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 위부터 시계 방향
dx = [0, 1, 1, 1, -1, -1, 0, -1]
dy = [1, 1, 0, -1, 0, -1, -1, 1]

def dfs(x, y):
  visited[x][y]=1
  
  if graph[x][y] == 1:
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      
      # 영역 내에 있으면서
      if 0 <= nx < h and 0 <= ny < w:
        if graph[nx][ny]==1 and not visited[nx][ny]:
          dfs(nx, ny)
        

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  
  graph = []
  visited = [[0] * w for _ in range(h)]
  answer = 0
  
  for _ in range(h):
    graph.append(list(map(int, input().split())))

  for x in range(h):
    for y in range(w):
      if not visited[x][y] and graph[x][y]==1:
        dfs(x, y)
        answer += 1
      else:
        continue
  print(answer)
