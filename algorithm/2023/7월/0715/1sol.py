# 백준 1715 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import heapq as hq
import sys

n = int(input())
arr = list()

for _ in range(n):
    hq.heappush(arr,int(sys.stdin.readline().rstrip()))

answer = 0
while len(arr) >= 2:
    value1 = hq.heappop(arr)
    value2 = hq.heappop(arr)
    value3 = value1+value2
    answer += value3
    hq.heappush(arr, value3)

if n == 1:
    print(0)
else:
    print(answer)