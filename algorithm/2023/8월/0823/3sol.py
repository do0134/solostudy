# 백준 16234 인구 이동

from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]


def bfs(r,c):
    global flag, dq
    q = deque()
    q.append((r,c))
    plus = list()
    cnt = 1
    value = arr[r][c]
    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr,nc = cr+dr[d], cc+dc[d]
            if 0 <= nr < n and 0 <= nc < n and not v[nr][nc]:
                if L <= abs(arr[cr][cc] - arr[nr][nc]) <= R:
                    q.append((nr,nc))
                    v[nr][nc] = 1
                    plus.append((nr,nc))
                    cnt += 1
                    value += arr[nr][nc]

    if not plus:
        return
    else:
        flag = True
        plus.append((r,c))
        value //= cnt
        for rr, ccc in plus:
            arr[rr][ccc] = value
            dq.append((rr,ccc))
        return


n, L, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = 0
flag = True
dq = deque([(i,j) for i in range(n) for j in range(n)])

while flag:
    flag = False
    v = [[0]*n for _ in range(n)]
    l = len(dq)
    for _ in range(l):
        r,c = dq.popleft()
        if not v[r][c]:
            v[r][c] = 1
            bfs(r,c)
    if flag:
        answer += 1

print(answer)