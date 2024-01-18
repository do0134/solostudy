# 백준 1946 신입사원

from collections import defaultdict
import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input())
    candidate = defaultdict(int)

    for _ in range(n):
        document, interview = map(int,input().split())
        candidate[document] = interview

    answer = 1
    min_v = candidate[1]

    for i in range(2,n+1):
        if candidate[i] < min_v:
            min_v = candidate[i]
            answer += 1

    print(answer)