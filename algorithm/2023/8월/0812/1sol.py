from collections import deque

dc = [-1,-1,0]
dr = [0,-1,-1]


def set_first(a,b,c):
    global bug
    amount = [[0] * n for _ in range(n)]
    idx = n-1
    flag = False

    for i in range(a):
        if not flag:
            idx -= 1
            if not idx:
                flag = True
        if flag:
            idx += 1

    for i in range(b):
        if not flag:
            amount[idx][0] = 1
            bug[idx][0] += 1
            idx -= 1
            if not idx:
                flag = True
        if flag:
            amount[0][idx] = 1
            bug[0][idx] += 1
            idx += 1

    for i in range(c):
        if not flag:
            amount[idx][0] = 2
            bug[idx][0] += 2
            idx -= 2
            if not idx:
                flag = True
        if flag:
            amount[0][idx] = 2
            bug[0][idx] += 2
            idx += 2

    bfs(amount)


def bfs(amount):
    global bug
    q = deque()
    q.append((1,1))
    v = [[0]*n for _ in range(n)]
    while q:
        cr,cc = q.popleft()
        value = 0
        for d in range(3):
            nr, nc = cr+dr[d], cc+dc[d]
            if 0 < nr <= n-1 and 0 < nc <= n-1:
                pass



n,day = map(int,input().split())
bug = [[1]*n for _ in range(n)]

for _ in range(day):
    a,b,c = list(map(int,input().split()))
    set_first(a,b,c)


