import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
num = defaultdict(int)

s,e = 0, 1
value = 0
answer = 0

while e < n:
    if s == e:
        e += 1
        if e == n:
            break

    if not num[arr[e]]:
        num[arr[e]] = e
        value += 1
        e += 1
        answer += value
    else:
        pass