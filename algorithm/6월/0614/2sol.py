# 백준 20225 Contact Tracer

import sys
input = sys.stdin.readline

while True:
    m,n,p = map(int,input().split())

    if m == 0 and n == 0 and p == 0:
        break

    v = set()
    v.add(p)

    for _ in range(n):
        a,b = map(int,input().split())
        if a in v:
            v.add(b)
        if b in v:
            v.add(a)

    print(len(v))

