from collections import deque
import sys

# 백준 2623 음악프로그램
input = sys.stdin.readline

n,m = map(int,input().split())
degree = [0]*(n+1)
tree = [set() for _ in range(n+1)]

for _ in range(m):
    arr = list(map(int,input().split()))
    for i in range(1,arr[0]):
        temp = len(tree[arr[i]])
        tree[arr[i]].add(arr[i+1])
        if temp != len(tree[arr[i]]):
            degree[arr[i+1]] += 1

q = deque()

for i in range(1,n+1):
    if not degree[i]:
        q.append(i)

answer = list()

while q:
    now = q.popleft()
    answer.append(now)
    for next_singer in tree[now]:
        degree[next_singer] -= 1
        if not degree[next_singer]:
            q.append(next_singer)

for i in range(1,n+1):
    if degree[i]:
        print(0)
        break
else:
    for i in answer:
        print(i)