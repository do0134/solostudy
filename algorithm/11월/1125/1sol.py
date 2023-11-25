# 백준 2468 안전영역

from collections import deque, defaultdict

dr = [1,-1,0,0]
dc = [0,0,1,-1]

n = int(input())
max_v = 0

maps = list()

for i in range(n):
    arr = list(map(int,input().split()))
    max_v = max(max_v, max(arr))
    maps.append(arr)

answer = 1

for i in range(max_v+1):
    v = defaultdict(bool)
    cnt = 0
    for i in range(n):
        for j in range(n):
            q = deque()
            
            if maps[i][j] > 1 and not v[(i,j)]:
                maps[i][j] -= 1
                q.append((i,j))
                v[(i,j)] = True
                
                while q:
                    cr,cc = q.popleft()
                    for d in range(4):
                        nr,nc = cr+dr[d], cc+dc[d]
                        if 0 <= nr < n and 0 <= nc < n and not v[(nr,nc)] and maps[nr][nc] > 1:
                            v[(nr,nc)] = True
                            q.append((nr,nc))
                
                cnt += 1
            else:
                maps[i][j] -= 1
    answer = max(cnt, answer)

print(answer)
