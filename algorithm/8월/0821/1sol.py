# 백준 13023 ABCDE

import sys
sys.setrecursionlimit(10**9)


def dfs(idx,cnt):
    global flag
    if flag:
        return

    for next_idx in tree[idx]:
        if not v[next_idx] and not flag:
            if cnt == 4:
                flag = True
                return
            else:
                v[next_idx] = 1
                dfs(next_idx,cnt+1)
                v[next_idx] = 0


n, m = map(int,input().split())
tree = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

v = [0]*n
flag = False

for i in range(n):
    v[i] = 1
    dfs(i,1)
    v[i] = 0
    if flag:
        break

if flag:
    print(1)
else:
    print(0)