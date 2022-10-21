import heapq as h

def Dik(start, end):
    q = list()
    v = [int(1e9)]*(n+1)
    v[start] = 0
    h.heappush(q,(start,0))
    while q:
        cc, cw = h.heappop(q)
        if v[cc] < cw:
            pass
        else:
            for nc,nw in tree[cc]:
                if v[nc] >= v[cc]+nw:
                    v[nc] = v[cc]+nw
                    h.heappush(q,(nc,v[nc]))
    return v[end]

n,m = map(int,input().split())
tree = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,w = map(int,input().split())
    tree[s].append((e,w))
    tree[e].append((s,w))

v1,v2 = map(int,input().split())

a = Dik(1,v1) + Dik(v1,v2) +Dik(v2,n)
b = Dik(1,v2) + Dik(v2,v1) + Dik(v1,n)

if min(a,b) >= int(1e9):
    print(-1)
else:
    print(min(a,b))

