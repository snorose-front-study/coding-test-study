# S1 영역 구하기
from collections import deque
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 상, 하, 좌, 우
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# BFS 알고리즘
# queue를 활용해 현재 위치에서 상하좌우로 이동하며 영역 탐색
# 중복 탐색을 방지하기 위해 visited를 활용하여 방문 여부 체크
# 탐색 시간 : O(NM)
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1  # 탐색한 영역의 크기

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in direction:
            nx = cx + dx
            ny = cy + dy
            if (
                0 <= nx < M
                and 0 <= ny < N
                and not visited[nx][ny]
                and field[nx][ny] == 0
            ):
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1

    return size


M, N, K = map(int, input().split())  # 세로 M, 가로 N, K개의 직사각형
field = [[0] * N for _ in range(M)]  # '1'이 직사각형에 해당하는 영역이 됨
visited = [[False] * N for _ in range(M)]  # 방문 여부

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())  # 왼쪽 (x, y) 좌표, 오른쪽 (x, y) 좌표

    for i in range(y1, y2):  # 아래 방향이 +인 y축
        for j in range(x1, x2):
            field[i][j] = 1

area = []
for i in range(M):
    for j in range(N):
        if (
            field[i][j] == 0 and not visited[i][j]
        ):  # 빈 영역이면서 방문을 안 한 경우 탐색
            area_size = bfs(i, j)
            area.append(area_size)

area.sort()
print(len(area))  # 영역 개수
print(*area)  # 영역 크기 출력
