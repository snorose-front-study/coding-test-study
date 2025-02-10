# S1 미로 탐색

import sys
from collections import deque

input = sys.stdin.readline


# BFS 알고리즘
def bfs(x, y):
    queue = deque([(x, y)])

    # 상, 하, 좌, 우로 이동 가능(근접 이동 조건)
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in direction:
            nx = cx + dx
            ny = cy + dy
            if (
                0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1
            ):  # NxM 내에 존재하고 미로의 해당 값이 1일때 이동 가능
                queue.append((nx, ny))
                # 최단 거리 값 갱신 (이로 인해 방문 여부 확인 리스트 불필요)
                maze[nx][ny] = maze[cx][cy] + 1

    # 도착지점의 최종 저장된 값이 최단 거리가 됨
    return maze[N - 1][M - 1]


N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

print(bfs(0, 0))
