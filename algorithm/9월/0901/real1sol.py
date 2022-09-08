import heapq as hq

def solve(type, u, v):
    global answer
    if type == 1:
        for i in tree[idx[u][0]]:
            if i[0] == idx[u][1] and i[1] == idx[u][2]:
                i[1] = v

                return
        pass
    elif type == 2 :
        v = [0]*(n+1)
        dp = [int(1e9)] * (n+1)

        pass

n = int(input())
tree = [[] for _ in range(n+1)]
idx = [[0]]
for _ in range(n-1):
    s,e,w = map(int,input().split())
    tree[s].append([e,w])
    idx.append([s,e,w])
m = int(input())
answer = list()
for _ in range(m):
    T,U,V = map(int,input().split())
    solve(T,U,V)