# 1939 중량제한

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = list()

for _ in range(m):
    s,e,w = map(int,input().split())
    graph.append((s,e,w))

S, E = map(int,input().split())

parent = [i for i in range(n+1)]
rank = [0]*(n+1)

graph.sort(key=lambda x:-x[2])


def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x1, x2):
    p1 = find(x1)
    p2 = find(x2)

    if p1 == p2:
        return

    if rank[p1] > rank[p2]:
        parent[p2] = p1
    elif rank[p1] < rank[p2]:
        parent[p1] = p2
    else:
        parent[p2] = p1
        rank[p1] += 1


answer = 0

for s,e,w in graph:
    if parent[s] != parent[e]:
        union(s,e)
        answer = w
    if find(S) == find(E):
        break

print(answer)