# 백준 1189 컴백홈
# https://www.acmicpc.net/problem/1189

dr = [1,-1,0,0]
dc = [0,0,1,-1]


def dfs(cr,cc,cnt,v):
    global answer

    if cnt > k:
        return

    if not cr and cc == c-1:
        if cnt == k:
            answer += 1
        return

    for d in range(4):
        nr,nc = cr+dr[d],cc+dc[d]
        if 0 <= nr < r and 0 <= nc < c and not v[nr][nc] and road[nr][nc] != "T":
            v[nr][nc] = 1
            dfs(nr,nc,cnt+1,v)
            v[nr][nc] = 0


r,c,k = map(int,input().split())
road = [list(input()) for _ in range(r)]
visit = [[0]*c for _ in range(r)]
visit[r-1][0] = 1
answer = 0
dfs(r-1,0,1,visit)

print(answer)