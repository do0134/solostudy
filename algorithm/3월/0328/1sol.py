# 백준 2533 사회망 서비스

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
dp = list()
dp.append([0]*(n+1))
dp.append([1]*(n+1))
visit = [0]*(n+1)

for _ in range(n-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)


def dfs(now, parent):
    visit[now] = 1
    if not len(tree[now]):
        return
    for next_node in tree[now]:
        if next_node != parent and not visit[next_node]:
            dfs(next_node, now)
            dp[0][now] += dp[1][next_node]
            dp[1][now] += min(dp[0][next_node],dp[1][next_node])


dp[1][1] = 1
dfs(1,-1)
print(min(dp[0][1], dp[1][1]))