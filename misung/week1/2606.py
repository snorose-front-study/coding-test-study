computer = int(input())
network = int(input())
graph = [[] for i in range(computer + 1)]
visited = [0] * (computer + 1)

for i in range(network):
  a, b = map(int, input().split())
  graph[a] += [b]
  graph[b] += [a]

# 그래프 완성 후 DFS 구현
def dfs(n):
  visited[n] = 1 # 방문 표시
  for nx in graph[n]: # 해당 위치의 모든 원소들 탐색
    if visited[nx] == 0:
      dfs(nx) # 방문하지 않은 경우 탐색 (재귀호출)

dfs(1)
print(sum(visited) - 1) # 자기 자신 제외

# 전체 풀이 흐름
# 1. 노드와 간선을 의미하는 computer와 network를 입력받는다.
# 2. 입력받은 노드를 토대로 graph 배열과 visited 배열을 생성한다.
# 3. 각 원소에 방문 표시를 하고, 해당 원소 내의 원소들을 차례로 탐색한다.
# 4. 방문하지 않은 원소에 대해, 3번 과정을 반복한다.
# 5. visited 원소 내 1의 갯수를 더하되, 자기 자신을 제외한다.