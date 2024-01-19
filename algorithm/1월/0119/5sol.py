# 백준 1654 랜선 자르기

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = [int(input()) for _ in range(n)]

l = 0
r = max(arr)*2
answer = 0

while l <= r:
    mid = (l+r) // 2
    now = 0

    for i in arr:
        now += i // mid

    if now >= k:
        answer = mid
        l = mid + 1
    else:
        r = mid - 1

print(answer)


