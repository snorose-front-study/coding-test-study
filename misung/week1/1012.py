# 유기농 배추
import sys
sys.setrecursionlimit(10000) # DFS 재귀 깊이 설정 (기본 제한 해제)

def dfs(x, y):
  # 탐색할 x, y가 영역을 벗어나면 종료
  if x < 0 or x>=n or y < 0 or y>= m:
    return False
  
  # 영역 안에 있다면 방문
  # 방문해야하는 경우
  if graph[x][y] == 1:
    graph[x][y] = 0 # 방문처리
    
    # 상하좌우 이동하며 연결된 배추 탐색
    for i in range(4):
      dfs(x + dx[i], y + dy[i]) # 재귀호출
      
    return True # 새로운 배추 덩어리 발견
  return False

# 입력 받기
t = int(sys.stdin.readline()) # 테스트 케이스 갯수

dx = [-1, 1, 0, 0] # 상하 이동
dy = [0, 0, -1, 1] # 좌우 이동

# 한 텀이 테스트케이스 한 개
for _ in range(t):
  m, n, k = map(int, sys.stdin.readline().split())
  
  # 배추밭 초괴화 (0으로 채운 행렬)  
  graph = [[0] * m for _ in range(n)]

  for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    graph[y][x] = 1
    
  count = 0
    
  for i in range(n):
    for j in range(m):
      if dfs(i, j): # 새로운 덩어리 발견
        count += 1
          
  print (count)