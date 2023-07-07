# 백준 6087 레이저 통신
# https://www.acmicpc.net/problem/6087

from collections import deque
from copy import deepcopy

w,h = map(int,input().split())
laser = [list(input()) for _ in range(h)]
q = deque()
# 방문 배열에 방향별로 dp처럼 사용할 수 있는 딕셔너리를 채워넣을 예정
v = [[] for _ in range(h)]
my_dict = {0:int(1e9),1:int(1e9),2:int(1e9),3:int(1e9)}

# my_dict * w는 얕은 복사가 되기때문에 deepcopy로 넣어준다.
for i in range(h):
    for _ in range(w):
        v[i].append(deepcopy(my_dict))

# 시작점을 찾기
for i in range(h):
    for j in range(w):
        if laser[i][j] == "C":
            laser[i][j] = "."
            for d in range(4):
                q.append((i,j,0,d))
                v[i][j][d] = 0
            break
    if q:
        break

answer = int(1e9)
dr = [1,-1,0,0]
dc = [0,0,1,-1]

# bfs 최대 100*100에 방향 *4 해서 최대 40000번정도 돌 예정
while q:
    cr, cc, cnt, cd = q.popleft()
    # cnt가 answer보다 크다면 돌 필요없다.
    if cnt > answer:
        continue

    for d in range(4):
        nr,nc = cr+dr[d],cc+dc[d]
        if 0 <= nr < h and 0 <= nc < w:
            # 이전과 방향이 같다면, cnt를 그대로 가고 아니라면 +1을 한다.
            if cd == d:
                ncnt = cnt
            else:
                ncnt = cnt+1

            if laser[nr][nc] == "." and v[nr][nc][d] > ncnt and ncnt < answer:
                q.append((nr,nc,ncnt,d))
                v[nr][nc][d] = ncnt
            elif laser[nr][nc] == "C" and answer > ncnt:
                v[nr][nc][d] = ncnt
                answer = ncnt
                continue

print(answer)