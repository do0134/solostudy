# 백준 1941 소문난 칠공주

from itertools import combinations
from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]


def bfs(r,c, combi):
    global flag
    q = deque()
    q.append((r,c))
    v = [0] * 7
    v[0] = 1

    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr,nc = dr[d]+cr, dc[d]+cc

            if (nr,nc) in combi and not v[combi.index((nr,nc))]:
                q.append((nr,nc))
                v[combi.index((nr,nc))] = 1

    if 0 in v:
        return False
    else:
        return True


def check_s(combi):
    y_cnt = 0
    for r,c in combi:
        if arr[r][c] == "Y":
            y_cnt += 1

    if y_cnt >= 4:
        return False
    else:
        return True


arr = [list(input()) for _ in range(5)]
answer = 0
idx = [(i,j) for i in range(5) for j in range(5)]
for combi in combinations(idx, 7):
    flag = False
    if bfs(combi[0][0],combi[0][1], combi):
        if check_s(combi):
            answer += 1
print(answer)
"""
YSYSY
SYSYS
YSYSY
SYSYS
YSYSY
"""