import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

def bfs(maze, n, m):
    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS를 위한 큐 설정 (시작점: (0,0))
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        # 네 방향으로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 미로 범위를 벗어나면 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽(0)인 경우 지나갈 수 없음
            if maze[nx][ny] == 0:
                continue

            # 방문하지 않은 길(1)인 경우
            if maze[nx][ny] == 1:
                # 이전 위치 값 +1 (거리 업데이트)
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    # 목적지 도착 시 최단 거리 반환
    return maze[n-1][m-1]

print(bfs(maze, n, m))
