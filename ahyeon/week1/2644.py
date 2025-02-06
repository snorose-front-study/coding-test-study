# S2 촌수 계산
from collections import deque
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# BFS 알고리즘
# 가까운 노드부터 탐색하며, 탐색하는 단계(깊이)가 곹 촌수가 됨
# queue를 이용한 탐색 진행
def bfs(start, target):
    queue = deque([(start, 0)])  # (현재 노드, 촌수)
    visited = [False] * (n + 1)  # 방문 여부

    visited[start] = True  # 시작 방문 노드를 true로 변경
    while queue:
        node, cnt = queue.popleft()  # queue에서 노드와 깊이를 pop

        # target 노드에 도달하면 촌수 출력
        if node == target:
            return cnt

        # 연결된 노드 탐색
        for nn in graph[node]:
            if not visited[nn]:  # 방문하지 않았다면
                visited[nn] = True
                queue.append((nn, cnt + 1))  # 촌수 증가

    return -1  # 연결되지 않은 경우 -1


n = int(input())  # 전체 사람의 수
a, b = map(int, input().split())  # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
m = int(input())  # 부모 자식들 간의 관계의 개수
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


print(bfs(a, b))
