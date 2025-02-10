# S1 단지번호붙이기
import sys

sys.setrecursionlimit(10**6)  # 런타임에러 해결용 리밋설정
input = sys.stdin.readline


# DFS 알고리즘
def dfs(x, y):
    global cnt
    cnt += 1  # 집 수 증가
    field[x][y] = 0  # 방문한 곳은 0으로 표시

    # 상, 하, 좌, 우로 연결된 것만 인정
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and field[nx][ny] == 1:
            dfs(nx, ny)


N = int(input())

# N개의 줄을 입력받아 2차원 리스트로 저장
# 1. input().strip() : 입력받은 문자열의 앞뒤 공백 제거
# 2. map(int, input().split()) : 공백을 기준으로 문자열의 각 문자를 정수(int)로 반환
# 3. list(...) : map 객체를 리스트로 반환
field = [list(map(int, input().strip())) for _ in range(N)]

houses = []  # 단지에 속하는 집의 수를 저장할 리스트

for i in range(N):
    for j in range(N):
        if field[i][j] == 1:
            cnt = 0  # 집 수를 세기 위한 변수
            dfs(i, j)
            houses.append(cnt)

houses.sort()  # 오름차순 정렬

total = len(houses)
print(total)
for i in range(total):
    print(houses[i])  # 각 단지의 집 수 출력
