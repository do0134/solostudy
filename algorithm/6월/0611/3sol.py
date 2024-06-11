# codeforces Maximum Multiple Sum

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    max_v = 0
    answer = 2

    for i in range(2, n+1):
        k = n // i
        cur_v = i*(k*(k+1)) // 2

        if cur_v > max_v:
            max_v = cur_v
            answer = i
    print(answer)