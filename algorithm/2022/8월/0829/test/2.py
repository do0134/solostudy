# 일단 백트래킹 쓸것
# 모든 가능한 경우의 수 점검
# 거기가 가능한지 체크하고, 가능하다면 줄 세우고 ㄱㄱ
from collections import deque
import copy
def set_line(r,c,d,input_list):
    set_list = copy.deepcopy(input_list)
    if d == 0:
        for i in range(r + 1, n):
            set_list[i][c] = -1
    elif d == 1:
        for i in range(0,r):
            set_list[i][c] = -1
    elif d == 2:
        for i in range(c + 1, n):
            set_list[r][i] = -1
    elif d == 3:
        for i in range(0,c):
            set_list[r][i] = -1
    #print(set_list)
    return set_list



def check(r,c,check_list):
    up = down = right = left = True
    for i in range(r+1,n):
        if check_list[i][c] != 0:
            down = False
            break
    for i in range(0,r) :
        if check_list[i][c] != 0:
            up = False
            break
    for i in range(c+1,n):
        if check_list[r][i] != 0:
            right = False
    for i in range(0,c):
        if check_list[r][i] != 0:
            left = False
    return (down,up,right,left)


t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    core = 0
    graph = deque()
    answer = int(1e9)
    for i in range(1,n-1):
        for j in range(1,n-1):
            if arr[i][j] == 1:
                core += 1
                graph.append((i,j))
    q = deque()
    q.append((graph[0][0],graph[0][1],arr,0))
    while q :
        cr,cc,now,idx = q.popleft()
        poss = check(cr,cc,now)
        if idx == core:
            cnt = 0
            for i in now:
                cnt += i.count(-1)
            answer = min(answer,cnt)
        else:
            for i in range(4):
                if poss[i] == True:
                    next = set_line(cr,cc,i,now)
                    if idx +1 >= len(graph):
                        q.append((graph[idx][0],graph[idx][1],next,idx+1))
                    else:
                        q.append((graph[idx+1][0],graph[idx+1][1],next,idx+1))
    print(f'#{tc} {answer}')
