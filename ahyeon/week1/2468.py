# S1 안전 영역
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# DFS 알고리즘
def dfs(x, y, h):
    visited[x][y] = True

    # 상 하 좌 우
    direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and field[nx][ny] > h:
            dfs(nx, ny, h)


N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]  # 지도 높이 정보

# map함수를 활용해 지도 내 최적 탐색 높이 구하기(field의 각 행에 대해 max() / min() 적용)
max_height = max(map(max, field))
# min_height = min(map(min, field)) # 최적화 시에만 사용하기 (이거 쓰면 틀렸습니다 나옴)

# 최대 안전 영역 개수
safe_area = 0

for h in range(0, max_height + 1):
    visited = [[False] * N for _ in range(N)]  # 방문 여부 초기화
    safe_area_h = 0  # 현재 높이에서의 안전 영역 개수

    for i in range(N):
        for j in range(N):
            if field[i][j] > h and not visited[i][j]:  # 물에 잠기지 않은 곳 탐색
                dfs(i, j, h)
                safe_area_h += 1

    safe_area = max(safe_area, safe_area_h)  # 최대 안전 영역 개수 갱신

print(safe_area)
