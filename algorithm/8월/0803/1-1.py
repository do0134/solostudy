# softeer 사물인식 최소 면적 산출 프로그램
# https://softeer.ai/practice/info.do?idx=1&eid=531&sw_prbl_sbms_sn=232752

from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)


def dfs(key, max_x, max_y, min_x, min_y, square):
    global answer, k, color
    if key == k+2:
        answer = min(answer, square)
        return
    if color[key]:
        for nx, ny in color[key]:
            nmax_x, nmin_x = max(nx,max_x), min(nx,min_x)
            nmax_y, nmin_y = max(ny,max_y), min(ny,min_y)
            next_square = (nmax_x-nmin_x) * (nmax_y-nmin_y)
            if next_square < answer:
                dfs(key+1, nmax_x, nmax_y, nmin_x, nmin_y, next_square)
    else:
        dfs(key+1,max_x, max_y, min_x, min_y, square)


n,k = map(int,input().split())
color = defaultdict(list)
answer = int(1e9)

for _ in range(n):
    x,y,c = map(int,input().split())
    color[c].append((x,y))
idx = 1
while idx <= k:
    if color[idx]:
        break
    idx += 1
for x,y in color[1]:
    dfs(1,x,y,x,y,0)

print(answer)