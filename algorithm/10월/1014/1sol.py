from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def solution(board):
    n = len(board)
    v = [[int(1e9)] * n for _ in range(n)]
    q = deque()
    q.append((0, 0, -1,0))
    v[0][0] = 0

    while q:
        cr, cc, cd,cost = q.popleft()
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if abs(d-cd) == 2:
                pass
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 1:
                if cd == -1 or cd== d:
                    n_cost = cost+100
                    if n_cost <= v[nr][nc]:
                        v[nr][nc] = n_cost
                        q.append((nr,nc,d,n_cost))

                elif d!= cd :
                    n_cost = cost+600
                    if n_cost-400 <= v[nr][nc]:
                        v[nr][nc] = n_cost
                        q.append((nr,nc,d,n_cost))
    return v[n-1][n-1]

