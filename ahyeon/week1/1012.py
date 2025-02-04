# S2 유기농배추
import sys

sys.setrecursionlimit(10**8)  # 런타임에러 해결용 리밋설정


# DFS 알고리즘
def dfs(x, y):
    graph[x][y] = 0  # 방문한 곳은 0으로 처리
    # 상, 하, 좌, 우
    direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
            dfs(nx, ny)


T = int(sys.stdin.readline())  # 테스트 케이스 수
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())  # 가로길이, 세로길이, 위치
    graph = [[0] * M for _ in range(N)]

    for i in range(K):  # 배추가 있는 곳이 1
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):  # 배추 있고 방문하지 않은 곳 탐색
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
