# 백준 7562 나이트의 이동

from collections import deque

dr = [2,2,-2,-2,1,1,-1,-1]
dc = [1,-1,1,-1,2,-2,2,-2]


def bfs():
    if sr == tr and sc == tc:
        return 0

    q = deque()
    v = [[int(1e9)]*n for _ in range(n)]

    q.append((sr,sc,0))
    v[sr][sc] = 1

    while q:
        cr, cc, cnt = q.popleft()

        for d in range(8):
            nr, nc = dr[d]+cr, dc[d]+cc
            if 0 <= nr < n and 0 <= nc < n and v[nr][nc] > cnt+1:
                if nr == tr and nc == tc:
                    return cnt+1

                v[nr][nc] = 1
                q.append((nr,nc,cnt+1))


tc = int(input())

for _ in range(tc):
    n = int(input())
    sr, sc = map(int,input().split())
    tr, tc = map(int,input().split())
    print(bfs())

