import heapq as h
import copy
def dik(start):
    global v2
    q = list()
    h.heappush(q, (start,0,[start]))
    v = [int(1e9)] * (n + 1)
    v[start] = 0
    return_value = []
    dp = [0]*(n+1)
    while q:
        ce, cw,visit = h.heappop(q)
        for ne,nw in bus[ce]:
            if v[ne] > v[ce] + nw:
                new_v = copy.deepcopy(visit)
                new_v.append(ne)
                h.heappush(q,(ne,nw,new_v))
                if ne == v2 and v[ne] > v[ce] + nw :
                    return_value = new_v
                v[ne] = v[ce] + nw
            elif v[ne] == v[ce] + nw:
                if nw == 0 and not dp[ne]:
                    new_v = copy.deepcopy(visit)
                    new_v.append(ne)
                    h.heappush(q, (ne, nw, new_v))
                    if ne == v2 and v[ne] > v[ce] + nw:
                        return_value = new_v
                    v[ne] = v[ce] + nw
                    dp[ne] = 1



    return [v[v2],len(return_value), return_value]



n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    bus[s].append((e,w))

v1,v2 = map(int,input().split())
answer = dik(v1)
for i in answer:
    if type(i) == list:
        print(*i)
    else:
        print(i)
