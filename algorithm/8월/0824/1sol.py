from collections import deque
# BFS로 풀 예정
# 최대 높이가 9임으로 1~9를 for문으로 돌면서 높이보다 낮은 곳을 1씩 count할 예정
# BFS를 돌다가, 범위를 넘어간다면, 높이로 가둬져있지 않다고 판단, cnt를 모두 버림
# 범위를 벗어나지 않는다면 answer에 더해줌

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


