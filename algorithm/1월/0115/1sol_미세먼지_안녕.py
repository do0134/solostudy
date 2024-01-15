# 백준 17144 미세먼지 안녕!

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

dr = [1,-1,0,0]
dc = [0,0,1,-1]

r,c,t = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(r)]

dust = deque()
air_cleaner = list()

for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            dust.append((i,j))

        elif room[i][j] == -1:
            air_cleaner.append((i,j))


# 공기청정기의 순환은 정해져있기때문에 미리 만들어준다.
def make_air_flow(cleaners: list) -> defaultdict:
    air_flow = defaultdict(int)

    for i in range(2):
        cleaner = cleaners[i]
        if not i:
            direction = [2,1,3,0]
        else:
            direction = [2,0,3,1]

        cr, cc = cleaner[0], cleaner[1]+1
        d = 0
        while (cr != cleaner[0] or cc != cleaner[1]) and d < 4:
            air_flow[(cr,cc)] = direction[d]+1
            if 0 <= cr+dr[direction[d]] < r and 0 <= cc+dc[direction[d]] < c:
                cr = cr + dr[direction[d]]
                cc = cc + dc[direction[d]]
            else:
                d += 1

    return air_flow


# 미세먼지를 움직이는 함수
# (r,c)에 먼지가 얼마인지 저장한 dict 반환
def move_dust(dusts: deque) -> defaultdict:
    dust_sum = defaultdict(int)

    while dusts:
        cr, cc = dusts.popleft()
        cnt = 0
        value = room[cr][cc] // 5

        for d in range(4):
            nr, nc = dr[d]+cr, dc[d]+cc
            if 0 <= nr < r and 0 <= nc < c and room[nr][nc] != -1:
                cnt += 1
                dust_sum[(nr, nc)] += value

        dust_sum[(cr,cc)] += room[cr][cc] - (value*cnt)
        room[cr][cc] = 0

    return dust_sum


# 공기 청정기
def clean_air(dusts: defaultdict, flow: defaultdict) -> defaultdict:
    new_dust = defaultdict(int)

    for key, value in dusts.items():
        cr, cc = key
        direction = flow[(cr,cc)]
        nr, nc = cr + dr[direction-1], cc + dc[direction-1]

        # 만약에 공기청정기에 닿는다면 무시
        if direction and (nr, nc) in air_cleaner:
            continue
        # 공기청정기에 닿지 않으면서 움직이는 먼지
        if direction and 0 <= nr < r and 0 <= nc < c:
            new_dust[(nr, nc)] = dusts[(cr,cc)]
        # 공기청정기와 상관없는 먼지
        elif not direction:
            new_dust[(cr,cc)] = dusts[(cr,cc)]

    return new_dust


def set_room(dusts: defaultdict):
    for key, value in dusts.items():
        cr, cc = key
        room[cr][cc] = value
        dust.append(key)


air_flow = make_air_flow(air_cleaner)
time = 0
while time < t:
    after_move = move_dust(dust)
    now = clean_air(after_move, air_flow)
    set_room(now)

    time += 1

answer = 0

for cr, cc in dust:
    answer += room[cr][cc]


print(answer)