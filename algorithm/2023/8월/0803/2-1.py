from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)


def dfs(idx, node, visit):
    if visit[idx]:
        return
    visit[idx] = 1
    for next_idx in node[idx]:
        dfs(next_idx,node,visit)


n,m = map(int,input().split())
node1 = defaultdict(list)
node2 = defaultdict(list)
for i in range(m):
    s,e = map(int,input().split())
    node1[s].append(e)
    node2[e].append(s)

S, T = map(int,input().split())
v1 = [0]*(n+1)
v2 = [0]*(n+1)
v3 = [0]*(n+1)
v4 = [0]*(n+1)

v1[T] = 1
dfs(S,node1,v1)
v2[S] = 1
dfs(T,node1,v2)
dfs(S,node2,v3)
dfs(T,node2,v4)

answer = 0
for i in range(1,n+1):
    if i == S or i == T:
        continue
    elif v1[i] and v2[i] and v3[i] and v4[i]:
        answer += 1

print(answer)