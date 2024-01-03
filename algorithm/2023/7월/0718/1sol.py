# 백준 2812 크게 만들기
# https://www.acmicpc.net/problem/2812

import sys

n,k = map(int,input().split())
s = sys.stdin.readline().rstrip()
answer = list()

for i in s:
    while answer and k > 0 and answer[-1] < i:
        answer.pop()
        k -= 1
    answer.append(i)
while k > 0:
    answer.pop()
    k -= 1

print("".join(answer))