# 백준 1068 트리

from collections import deque

n = int(input())
arr = list(map(int,input().split()))
target = int(input())

tree = [[] for _ in range(n)]
start = -1

for i, parent in enumerate(arr):
    if parent == target or i == target:
        continue

    if parent == -1:
        start = i
        continue

    tree[parent].append(i)

q = deque()

if start != -1:
    q.append(start)

answer = 0

while q:
    now_idx = q.popleft()

    for next_idx in tree[now_idx]:
        if not tree[next_idx]:
            answer += 1

        q.append(next_idx)

    if now_idx == start and not q:
        answer += 1

print(answer)