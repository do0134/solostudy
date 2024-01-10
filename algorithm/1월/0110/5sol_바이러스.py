# 백준 2606 바이러스
# https://www.acmicpc.net/problem/2606

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

network = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    network[s].append(e)
    network[e].append(s)

v = [0]*(n+1)
stack = list()
stack.append(1)
v[1] = 1
cnt = 0
while stack:
    now = stack.pop()

    for next_computer in network[now]:
        if not v[next_computer]:
            stack.append(next_computer)
            v[next_computer] = 1
            cnt += 1

print(cnt)