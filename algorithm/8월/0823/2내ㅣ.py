# 백준 2493 탑

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
answer = [0]*n
dq = deque()
for i in range(n-1,-1,-1):
    if not dq:
        dq.append((arr[i],i))

    elif dq[-1][0] <= arr[i]:
        while dq and dq[-1][0] <= arr[i]:
            h, idx = dq.pop()
            answer[idx] = i+1
        dq.append((arr[i],i))
    else:
        dq.append((arr[i],i))


print(*answer)