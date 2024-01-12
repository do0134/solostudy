# 백준 11725 트리의 부모 찾기

import sys
input = sys.stdin.readline


n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    node1, node2 = map(int,input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

parent = [0]*(n+1)
parent[1] = 1

stack = list()
stack.append(1)

while stack:
    now_node = stack.pop()

    for next_node in tree[now_node]:
        if not parent[next_node]:
            parent[next_node] = now_node
            stack.append(next_node)

for parent_node in parent[2:]:
    print(parent_node)