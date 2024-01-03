# 백준 14503 로봇 청소기

N,M = map(int,input().split())
R,C,D = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]
answer = 0
stack = [(R,C,D)]

direction = {0: "wsen", 1: "nwse", 2:"enws", 3: "senw"}
base_d = ((-1,0),(0,1),(1,0),(0,-1))
idx = {"w": (0,-1), "s": (1,0), "e": (0,1), "n": (-1,0)}


def clean(r,c):
    global answer
    if not room[r][c]:
        answer += 1
        room[r][c] = 2


def dirty_check(r,c):
    for dr,dc in base_d:
        nr,nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M and not room[nr][nc]:
            return True
    return False


def move_back(r,c,d):
    nr,nc = r-base_d[d][0], c-base_d[d][1]
    if 0 <= nr < N and 0 <= nc < M and room[nr][nc] != 1:
        return nr, nc
    else:
        return -1, -1


def move_forward(r,c,d):
    for i in direction[d]:
        dr, dc = idx[i]
        nr,nc = r+dr, c+dc
        if 0 <= nr < N and 0 <= nc < M and not room[nr][nc]:
            return nr, nc, base_d.index(idx[i])


while stack:
    cr, cc, cd = stack.pop()
    clean(cr,cc)
    if not dirty_check(cr,cc):
        next_r, next_c = move_back(cr,cc,cd)
        if next_r == -1:
            break
        else:
            stack.append((next_r,next_c,cd))
    else:
        next_r, next_c, next_d = move_forward(cr,cc,cd)
        stack.append((next_r,next_c,next_d))

print(answer)
