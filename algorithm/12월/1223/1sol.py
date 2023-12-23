# 백준 15681 트리와 쿼리

from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, r, q = map(int,input().split())
tree = [[] for _ in range(n+1)]
leaf = defaultdict(int)

for _ in range(n-1):
    s, e = map(int,input().split())
    tree[s].append(e)
    tree[e].append(s)


def dfs(parent, now):
    value = 1
    for next_node in tree[now]:
        if next_node != parent:
            value += dfs(now, next_node)
    leaf[now] = value
    return value


dfs(-1,r)

for _ in range(q):
    query = int(input())
    print(leaf[query])
