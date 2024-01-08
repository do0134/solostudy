# 백준 1715 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import sys
import heapq as hq

input = sys.stdin.readline

n = int(input().rstrip())
heap = list()

for _ in range(n):
    num = int(input())
    hq.heappush(heap, num)

answer = 0

while heap and len(heap) > 1:
    a = hq.heappop(heap)
    b = hq.heappop(heap)
    hq.heappush(heap,a+b)
    answer += a+b

print(answer)

