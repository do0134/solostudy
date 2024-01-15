# 백준 16236 아기 상어

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
sea = list()
size = 2

dr = [1,-1,0,0]
dc = [0,0,1,-1]

for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        if temp[j] == 9:
            sr = i
            sc = j
            temp[j] = 0

    sea.append(temp)


def check(r: int, c: int) -> (list[tuple], int):
    v = [[int(1e9)]*n for _ in range(n)]
    v[r][c] = 0

    q = deque()
    q.append((r,c,0))

    min_distance = int(1e9)
    can_eat = list()

    while q:
        cr, cc, cnt = q.popleft()

        for d in range(4):
            nr, nc = cr+dr[d], cc+dc[d]
            if 0 <= nr < n and 0 <= nc < n and v[nr][nc] > cnt+1 and sea[nr][nc] <= size:
                if cnt+1 < min_distance and size > sea[nr][nc] > 0:
                    min_distance = cnt+1
                    can_eat = [(nr,nc)]
                elif cnt+1 == min_distance and size > sea[nr][nc] > 0:
                    can_eat.append((nr,nc))

                q.append((nr,nc,cnt+1))
                v[nr][nc] = cnt+1

    return can_eat, min_distance


for_size = 0
answer = 0

while True:
    check_fish, distance = check(sr, sc)
    if not check_fish:
        break

    check_fish.sort()
    answer += distance
    sr, sc = check_fish[0]
    sea[sr][sc] = 0

    for_size += 1
    if for_size == size:
        size += 1
        for_size = 0


print(answer)