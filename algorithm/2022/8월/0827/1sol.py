# 기본 bfs,dfs문제 dfs로 풀것
# 이중 for문을 돌려 방문하지 않은 1을 찾음
# cnt ++ 해주고, dfs를 돌림
# stack에 인자 하나를 추가할 때마다 사이즈를 1더하고, dfs가 끝날때 사이즈 확인


def dfs(r,c):
    global size
    stack = list()
    stack.append((r,c))
    v[r][c] = 1
    temp = 1
    while stack:
        cr,cc = stack.pop()
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < n and 0 <= nc < m and not v[nr][nc] and arr[nr][nc] == 1:
                stack.append((nr,nc))
                v[nr][nc] = 1
                temp += 1
    size = max(size,temp)



dr = [1,-1,0,0]
dc = [0,0,1,-1]

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
cnt = 0
size = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not v[i][j]:
            cnt += 1
            dfs(i,j)
print(cnt)
print(size)