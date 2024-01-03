# 프로그래머스 자물쇠와 열쇠

def rotate(key, m):
    new_key = [[0] * m for _ in range(m)]
    key_idx = list()
    for i in range(m):
        for j in range(m):
            new_key[j][m - i - 1] = key[i][j]
            if key[i][j]:
                key_idx.append((j, m - i - 1))

    return new_key, key_idx


def check(hole, r, c, key_idx, n):
    hole_v = [0] * len(hole)

    for i in range(len(key_idx)):
        cr, cc = key_idx[i]
        nr, nc = cr + r, cc + c
        if 0 <= nr < n and 0 <= nc < n:
            for j in range(len(hole)):
                if not hole_v[j] and hole[j] == (nr, nc):
                    hole_v[j] = 1
                    break

            if (nr, nc) not in hole:
                return False

    return bool(0 not in hole_v)


def solution(key, lock):
    answer = False
    n, m = len(lock), len(key)

    hole = list()

    for i in range(n):
        for j in range(n):
            if not lock[i][j]:
                hole.append((i, j))

    if not hole:
        return True

    for d in range(4):
        key, key_idx = rotate(key, m)
        if len(key_idx) < len(hole):
            return answer

        for i in range(-20, 20):
            for j in range(-20, 20):
                if check(hole, i, j, key_idx, n):
                    answer = True
                    return answer

    return answer