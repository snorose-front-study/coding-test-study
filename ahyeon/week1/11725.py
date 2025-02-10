# S2 트리의 부모 찾기
import sys
from collections import deque

input = sys.stdin.readline


# BFS 알고리즘
# 부모노드를 찾는 최단 거리 구하기에 적합
def bfs(root):
    queue = deque([root])

    while queue:
        node = queue.popleft()  # 현재 노드 꺼내기

        for i in tree[node]:  # 현재 노드와 연결된 노드들 꺼내기
            if not parent[i]:  # 부모노드가 없으면 부모를 설정하고 큐에 추가
                parent[i] = node
                queue.append(i)


N = int(input())
tree = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

bfs(1)

for i in range(2, N + 1):
    print(parent[i])
