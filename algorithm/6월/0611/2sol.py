# codeforces Creating Words

import sys 
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = input().split()
    c, d = "", ""
    c += b[0]
    d += a[0]
    for i in range(1,len(a)):
        c += a[i]
    for i in range(1,len(b)):
        d += b[i]
    print(c,d)