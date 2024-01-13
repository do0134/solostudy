import sys
input = sys.stdin.readline

n, m = map(int,input().split())
cities = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    cities[s].append((w,e))
    cities[e].append((w,s))


parent = [i for i in range(n+1)]
rank = [i for i in range(n+1)]


def find(x):
    if x == parent[x]:
        return x

    return find(parent[x])


def union(a,b):
    x = find(a)
    y = find(b)


