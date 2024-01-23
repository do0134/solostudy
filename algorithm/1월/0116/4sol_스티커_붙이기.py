import sys
input = sys.stdin.readline


def can_put(r,c,stick):

    space = list()

    for cr in range(len(stick)):
        for cc in range(len(stick[0])):
            if stick[cr][cc]:
                space.append((cr,cc))

    temp = list()

    for cr, cc in space:
        nr, nc = r+cr, c+cc
        if 0 <= nr < n and 0 <= nc < m and not book[nr][nc]:
            temp.append((nr,nc))
        else:
            return False
    for r_idx, c_idx in temp:
        book[r_idx][c_idx] = 1

    return True


def rotate(stick):
    temp = list()
    for i in zip(*stick[::-1]):
        temp.append(list(i))
    return temp


def put_sticker(stick):
    for i in range(n):
        for j in range(m):

            if can_put(i,j,stick):
                return True

    return False


n,m,k = map(int,input().split())
sticker = list()

for _ in range(k):
    r,c = map(int,input().split())
    temp = [list(map(int,input().split())) for _ in range(r)]
    sticker.append(temp)

book = [[0]*m for _ in range(n)]

for idx in range(k):
    for _ in range(4):
        if put_sticker(sticker[idx]):
            break

        sticker[idx] = rotate(sticker[idx])


answer = 0
for b in book:
    answer += b.count(1)

print(answer)