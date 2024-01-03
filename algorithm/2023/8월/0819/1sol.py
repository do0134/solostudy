# 백준 15235 Olympiad Pizza

from collections import deque

n = int(input())
arr = list(map(int,input().split()))
q = deque()
answer = [0]*n
idx = 1
for i,j in enumerate(arr):
    answer[i] = idx
    idx += 1
    if j-1 > 0:
        q.append((i,j-1))

while q:
    now, need = q.popleft()
    answer[now] = idx
    idx += 1
    if need-1 > 0:
        q.append((now,need-1))

print(*answer)