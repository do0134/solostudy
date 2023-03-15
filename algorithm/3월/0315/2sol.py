from collections import defaultdict

n = int(input())
tree = defaultdict(list)
dp = [[0,0] for _ in range(n+1)]
v = [0]*(n+1)
for _ in range(n-1) :
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

