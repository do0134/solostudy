# 프로그래머스 무인도 여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque


def solution(maps):
    answer = []
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    v = [[0] * len(maps[0]) for _ in range(len(maps))]
    q = deque()
    n = len(maps)
    m = len(maps[0])

    for i in range(n):
        for j in range(m):
            if not v[i][j] and maps[i][j] != "X":
                value = int(maps[i][j])
                q.append((i, j))
                v[i][j] = 1
                while q:
                    cr, cc = q.popleft()
                    for d in range(4):
                        nr, nc = dr[d] + cr, dc[d] + cc
                        if 0 <= nr < n and 0 <= nc < m and not v[nr][nc] and maps[nr][nc] != "X":
                            value += int(maps[nr][nc])
                            v[nr][nc] = 1
                            q.append((nr, nc))

                answer.append(value)

    if not answer:
        answer.append(-1)
    return sorted(answer)