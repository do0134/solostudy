# 백준 13484 Tarifa

import sys
input = sys.stdin.readline

x = int(input())
n = int(input())
answer = 0

for _ in range(n):
    answer += x
    temp = int(input())
    if temp > answer:
        answer = 0
    else:
        answer -= temp

print(answer+x)