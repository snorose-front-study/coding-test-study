import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 부모 정보 저장
parent = [0] * (n + 1)

# BFS 탐색
def bfs():
    queue = deque([1])  # 루트 노드부터 시작
    while queue:
        node = queue.popleft()
        for child in tree[node]:
            if parent[child] == 0:  # 아직 부모가 없는 경우 (= 방문하지 않은 경우)
                parent[child] = node
                queue.append(child)

bfs()
for i in range(2, n+1):
    print(parent[i])
