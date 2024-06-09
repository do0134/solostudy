# codeforces XOR Sequences

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    ans = 0

    while True:
        if (x ^ y) & 1:
            break

        ans += 1
        x >>= 1
        y >>= 1

    print(1 << ans)