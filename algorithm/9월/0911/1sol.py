# 프로그래머스 미로 탈출

from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def solution(maps):
    def bfs(r, c, target_r, target_c):
        q = deque()
        q.append((r, c, 0))
        v = [[0] * len(maps[0]) for _ in range(len(maps))]
        v[r][c] = 1

        while q:
            cr, cc, cnt = q.popleft()
            for d in range(4):
                nr, nc = cr + dr[d], cc + dc[d]
                if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and not v[nr][nc] and maps[nr][nc] != "X":
                    v[nr][nc] = cnt + 1
                    q.append((nr, nc, cnt + 1))

        return v[target_r][target_c]

    s = list()
    l = list()
    e = list()

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                s = [i, j]
            elif maps[i][j] == "L":
                l = [i, j]
            elif maps[i][j] == "E":
                e = [i, j]

    d1 = bfs(s[0], s[1], l[0], l[1])
    d2 = bfs(l[0], l[1], e[0], e[1])

    if not d1 or not d2:
        answer = -1
    else:
        answer = d1 + d2

    return answer