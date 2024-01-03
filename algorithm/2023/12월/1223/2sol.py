# 백준 15681 트리와 쿼리 2

import sys
input = sys.stdin.readline

n,r,q = map(int,input().split())
tree = [[] for _ in range(n+1)]
parents = [1]*(n+1)

for _ in range(n-1):
    u, v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

stack = [(r,-1)]
node = list()

while stack:
    now, parent = stack.pop()
    for next_node in tree[now]:
        if next_node != parent:
            stack.append((next_node, now))
            node.append((now, next_node))

for s, e in node[::-1]:
    parents[s] += parents[e]


for _ in range(q):
    query = int(input())
    print(parents[query])