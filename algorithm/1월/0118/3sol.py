# 백준 1946 신입사원

import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input())
    candidate = list()

    for _ in range(n):
        document, interview = map(int,input().split())
        candidate.append((document, interview))

    candidate.sort()
    answer = 1

    min_v = candidate[0][1]

    for i in range(1,n):
        if candidate[i][1] < min_v:
            min_v = candidate[i][1]
            answer += 1

    print(answer)