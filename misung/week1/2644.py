# 촌수계산 (DFS)

n = str(input())
a, b = map(int, input().split())
m = str(input())

# 전체사람 n에 대한 빈 배열 생성하기
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []

# 부모x와 자식y 입력받아 2차원 배열인 graph에 추가
for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)
  
# dfs
def dfs (v, num):
  num += 1
  visited[v] == True
  
  # 내가 찾던 그 사람이면
  if v == b:
    result.append(num)
    
  for i in graph[v]:
    if not visited[i]:
      dfs(i, num)
  
  
  
  
dfs (a, 0)

if(len(result) == 0):
  print(-1)
else:
  print(result[0] - 1)
