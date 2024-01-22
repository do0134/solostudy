from collections import defaultdict
import heapq as hq
import sys
input = sys.stdin.readline


d_idx = {1: -1, 2: 1, 3: 1, 4: -1}

# 해당 idx에서 가장 가까운 상어 잡기
def move_and_hit():
    global answer, M
    if not shark_idx:
        return []

    die = hq.heappop(shark_idx)
    print(die, "___________________________________")
    print(shark[die])
    # answer에 잡은 상어 크기 더해주기
    answer += shark[die][2]
    M -= 1
    # return한 r,c는 상어 이동할 때 사용할 예정
    return die


def eat_shark(idx1, idx2):

    if idx1[2] > idx2[2]:
        return idx1

    return idx2


def move_col(direct, cr, cc, speed):
    # 3,4일 때 반대로 계산해야 하기 때문에 두 번 나눠준다.
    if direct == 3:
        if speed < C-1 - cc:
            return cr, cc+speed, direct
        elif speed == C-1 - cc:
            return cr, C-1, 4

        speed -= C-1 - cc
        cc = C-1
        direct = 4
    else:
        if speed < cc-0:
            return cr, cc-speed, direct
        elif speed == cc - 0:
            return cr, 0, 3

        speed -= cc - 0
        cc = 0
        direct = 3

    value = speed // (C-1)
    mod = speed % (C-1)

    if value % 2:
        if direct == 3:
            direct = 4
        else:
            direct = 3

    cc += d_idx[direct] * mod

    return cr, cc, direct


def move_row(direct, cr, cc, speed):
    if direct == 2:
        if speed < R - 1 - cr:
            return cr + speed, cc, direct
        elif speed == R - 1 - cr:
            return R-1, cc, 1

        speed -= R - 1 - cr
        cr = R - 1
        direct = 1
    else:
        if speed < cr - 0:
            return cr - speed, cc, direct
        elif speed == cr - 0:
            return 0, cc, 2

        speed -= cr - 0
        cr = 0
        direct = 2

    value = speed // (R - 1)
    mod = speed % (R - 1)

    if value % 2:
        if direct == 2:
            direct = 1
        else:
            direct = 2

    cr += d_idx[direct] * mod

    return cr, cc, direct



# 상어 이동하고 중복 제거
def move_shark():
    if idx + 1 == C:
        return {}, []

    new_shark = dict()
    new_idx = list()
    temp = list()

    for key in shark.keys():
        cr, cc = key

        if (cr, cc) == die:
            continue

        cs,cd,cz = shark[key]
        if cd == 1 or cd == 2:
            nr,nc,nd = move_row(cd, cr, cc, cs)
        else:
            nr,nc,nd = move_col(cd, cr, cc, cs)

        if new_shark.get((nr,nc)):
            real = eat_shark(new_shark[(nr,nc)], (cs,nd,cz))
            new_shark[(nr,nc)] = real

        else:
            new_shark[(nr,nc)] = (cs,nd,cz)

        if nc == idx+1:
            temp.append(nr)

    for shark_r in temp:
        hq.heappush(new_idx, (shark_r, idx+1))

    return new_shark, new_idx


R,C,M = map(int,input().split())

shark = defaultdict(tuple)
shark_idx = list()
answer = 0

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    shark[(r-1,c-1)] = (s,d,z)
    if not c-1:
        hq.heappush(shark_idx, (r-1, c-1))

idx = 0
while idx < C:
    if not M:
        break
    print(idx, answer, "++++++++++")
    print(shark)
    die = move_and_hit()
    n_shark, n_idx = move_shark()
    shark, shark_idx = n_shark, n_idx
    idx += 1
print(answer)