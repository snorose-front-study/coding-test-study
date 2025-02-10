import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

count = 0

def dfs(x, y):
  # 8가지 방향(가로, 세로, 대각선)으로 이동하는 dx, dy 리스트 정의
  dx = [1, 1, -1, -1, 1, -1, 0, 0]
  dy = [0, 1, 0, 1, -1, -1, 1, -1]

  field[x][y] = 0 # 방문한 땅(1)을 바다(0)로 바꿔 중복 방문 방지
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1: # 지도 범위 내이고, 방문하지 않은 땅(1)인 경우
      dfs(nx, ny)

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  field = [] # 지도 배열
  count = 0 # 섬 개수
  for _ in range(h):
    field.append(list(map(int, input().split())))
  for i in range(h):
    for j in range(w):
      if field[i][j] == 1:
        dfs(i, j)
        count += 1

print(count)