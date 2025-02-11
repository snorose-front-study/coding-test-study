# S5 크로아티아 알파벳
import sys

input = sys.stdin.readline

word = input().strip()
cnt = len(word)

for i in range(cnt):
    if i > 0 and word[i] == "=":
        if word[i - 1] == "c" or word[i - 1] == "s":
            cnt -= 1
        elif word[i - 1] == "z":
            cnt -= 1
            if i > 1 and word[i - 2] == "d":
                cnt -= 1
    elif i > 0 and word[i] == "-":
        if word[i - 1] == "c" or word[i - 1] == "d":
            cnt -= 1
    elif i > 0 and word[i] == "j":
        if word[i - 1] == "l" or word[i - 1] == "n":
            cnt -= 1

print(cnt)

# 위의 코드의 문제점 :
# 1. if문을 돌아 검사를 하기 때문에 불필요한 연산이 추가됨 (O(N^2)에 가까운 비효율적인 연산 발생)
# 2. word[i]를 계속 검사해야 함. 'dz='의 경우 추가적 예외 처리 필요

# => replace()를 활용해 효율적인 코드를 작성할 수 있음
# replace() 함수는 O(N)의 시간 복잡도로 동작함 & 함수가 C로 구현되어 있어 빠르게 동작함


# 크로아티아 알파벳 리스트
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in croatia:
    word = word.replace(c, "*")  # 크로아티아 알파벳을 "*"로 변환

print(len(word))
