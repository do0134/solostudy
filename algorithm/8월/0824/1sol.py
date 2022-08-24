from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def bfs(row,col,h):
    global answer
    q = deque()
    q.append((row,col))
    flag = False
    cnt = 1
    v[row][col] = 1
    while q :
        cr,cc = q.popleft()
        for d in range(4):
            nr = dr[d] + cr
            nc = dc[d] + cc
            if 0 <= nr < n and 0 <= nc < m :
                if not v[nr][nc] and pool[nr][nc]<=h:
                    q.append((nr,nc))
                    v[nr][nc] = 1
                    cnt += 1
            else:
                flag = True

    if flag:
        return
    else:
        answer += cnt
        return

n, m = map(int,input().split())
pool = [list(map(int,input())) for _ in range(n)]
answer = 0


for i in range(1,10):
    v = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if pool[r][c] <= i and not v[r][c]:
                bfs(r,c,i)


print(answer)


