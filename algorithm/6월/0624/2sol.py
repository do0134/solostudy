# codeforces Matrix Stabilization

import sys
input = sys.stdin.readline

t = int(input())
dr = [1,-1,0,0]
dc = [0,0,1,-1]




for _ in range(t):
    n,m = map(int,input().split())
    answer = [list(map(int,input().split())) for _ in range(n)]
    
    def check(arr):
        new_arr = list()
        for r,c in arr:
            for_check = 0
            for d in range(4):
                nr, nc = dr[d] + r, dc[d] + c
                if 0 <= nr < n and 0 <= nc < m:
                    for_check += 1
                    if answer[nr][nc] > answer[r][c]:
                        break
            else:
                if for_check:
                    new_arr.append((r,c))

        return new_arr
    
    def execute(arr):
        for r,c in arr:
            answer[r][c] -= 1

    
    flag = True
    temp = list()
    for i in range(n):
        for j in range(m):
            temp.append((i,j))

    n_arr = check(temp)
    if not n_arr:
        flag = False

    while flag:
        execute(n_arr)
        n_arr = check(n_arr)
        if not n_arr:
            flag = False
        print(11)
    for i in answer:
        print(*i)

    