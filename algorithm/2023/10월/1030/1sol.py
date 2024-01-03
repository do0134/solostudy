# 백준 7562 나이트의 이동

from collections import deque

dr = [2, 1, -1, -2, -2, -1, 1, 2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

t = int(input())
for _ in range(t):
    l = int(input())
    s,e = map(int,input().split())
    ts, te = map(int,input().split())

    if s == ts and e == te:
        print(0)
        continue
    q = deque()
    v = [[0]*l for _ in range(l)]
    v[s][e] = 1
    q.append((s,e,0))

    while q:
        cr,cc,cnt = q.popleft()

        for d in range(8):
            nr,nc = dr[d] + cr, dc[d] + cc
            if 0 <= nr < l and 0 <= nc < l and v[nr][nc] < cnt+1:
                q.append((nr,nc,cnt+1))
                v[nr][nc] = cnt+1

        if v[ts][te]:
            print(v[ts][te])
            break