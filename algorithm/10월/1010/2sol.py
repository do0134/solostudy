# 프로그래머스 퍼즐 조각 채우기

from collections import deque


def correct_idx(arr):
    min_r, min_c = int(1e9), int(1e9)
    val = list()

    for r, c in arr:
        min_r = min(min_r, r)
        min_c = min(min_c, c)

    for r, c in arr:
        nr = r - min_r
        nc = c - min_c
        val.append((nr, nc))
    val.sort()
    return val


def bfs(arr, ver):
    n = len(arr)
    v = [[0] * n for _ in range(n)]
    val = list()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == ver and not v[i][j]:
                q = deque()
                q.append((i, j))
                v[i][j] = 1
                new_val = [(i, j)]

                while q:
                    cr, cc = q.popleft()
                    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < n and 0 <= nc < n and not v[nr][nc] and arr[nr][nc] == ver:
                            q.append((nr, nc))
                            v[nr][nc] = 1
                            new_val.append((nr, nc))
                correct_val = correct_idx(new_val)
                val.append(correct_val)

    return val


def rotate(arr, n):
    val = list()
    for r, c in arr:
        val.append((c, n - 1 - r))
    val = correct_idx(val)
    return val


def is_valid(hole, block):
    if len(hole) != len(block):
        return False
    for idx in hole:
        if idx not in block:
            return False

    return True


def solution(game_board, table):
    answer = 0
    n = len(game_board)
    blocks = bfs(table, 1)
    holes = bfs(game_board, 0)
    v = [0] * len(holes)
    for block in blocks:
        for i in range(len(holes)):
            if not v[i]:
                hole = holes[i]
                val = hole
                flag = False
                for _ in range(4):
                    val = rotate(val, n)
                    if is_valid(val, block):
                        answer += len(val)
                        v[i] = 1
                        flag = True
                        break
                if flag:
                    break

    return answer