import heapq as h

n,m = map(int,input().split())
tree = [[] for _ in range(n+1)]
v = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s,e,w = map(int,input().split())
    tree[s].append((e,w))
    tree[e].append((s,w))

v1,v2 = map(int,input().split())

q = list()
for i in tree[1]:
    h.heappush(q,(i[0],i[1]))

