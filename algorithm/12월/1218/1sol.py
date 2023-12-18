# 백준 2785 체인

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
answer = 0

total = n
cnt = 1

for i in range(n):
    if arr[i]+cnt >= total:
        break
    else:
        cnt += arr[i]
        total -= 1


print(total-1)