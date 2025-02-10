# S2 섬의 개수
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# DFS 알고리즘
def dfs(x, y):
    field[x][y] = 0  # 방문 여부 표시 (방문했으면 0으로 변경)
    # 가로, 세로, 대각선으로 이동할 수 있으면 하나의 섬으로 취급
    direction = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        # 가로, 세로, 대각선에 1이 있는 경우에만 dfs알고리즘 적용
        if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
            dfs(nx, ny)


ans = []  #  '0 0'이 나오기 전까지 답변을 저장할 리스트
while True:
    w, h = map(int, input().split())  # 너비 w, 높이 h
    if w == 0 and h == 0:
        break

    field = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0  # 섬의 개수
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                dfs(i, j)
                cnt += 1
    ans.append(cnt)

for i in range(len(ans)):  # 저장된 답변 출력
    print(ans[i])
