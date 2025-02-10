"""
Input: N(단어의 개수) / word(N개의 단어)
Output:
Constraints: 1 <= N <= 100 / len(word) <= 100
"""
import sys

input = sys.stdin.readline

# 입력
N = int(input())
count = N

for i in range(N):
  word = input()
  for j in range(0, len(word)-1):
    if word[j] == word[j+1]: # 현 문자열이 바로 뒤의 문자열과 같은 경우
      pass
    elif word[j] in word[j+1:]: # 현 문자열이 바로 뒤의 문자열과 다른데, 이후 문자열에 해당 문자열이 나타나는 경우
      count -= 1
      break

print(count)