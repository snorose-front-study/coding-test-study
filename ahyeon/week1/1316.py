# S5 그룹 단어 체커
import sys

input = sys.stdin.readline

N = int(input())  # 주어진 단어의 개수
cnt = 0  # 그룹 단어의 개수

for _ in range(N):
    word = input().rstrip()
    stack = []  # 등장한 알파벳을 저장할 리스트
    is_group = True  # 그룹 단어인지 판단하는 flag

    for i in range(len(word)):
        if word[i] not in stack:  # 처음 등장하는 단어면 stack에 저장
            stack.append(word[i])
        elif (
            word[i] in stack and word[i] != word[i - 1]
        ):  # 이미 등장했던 알파벳이고 직전의 알파벳과 다르면 break
            is_group = False
            break

    if is_group:
        cnt += 1

print(cnt)
