# codeforces x-axis

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b,c = map(int,input().split())
    min_v = int(1e9)
    for i in range(1, 11):
        min_v = min(min_v, abs(a-i) + abs(b-i) + abs(c-i))

    print(min_v)