# 백준 11060 점프 점프
# https://www.acmicpc.net/problem/11060

from collections import deque

n = int(input())
arr = [0]+list(map(int,input().split()))
v = [int(1e9)]*(n+1)

q = deque()
q.append(1)
v[1] = 0

while q:
    curr = q.popleft()
    next = curr+arr[curr]

    for idx in range(curr+1,min(next+1,n+1)):
        if v[idx] > v[curr]+1:
            v[idx] = v[curr]+1
            q.append(idx)

if v[-1] == int(1e9):
    v[-1] = -1
print(v[-1])