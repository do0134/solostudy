def solve(idx, showm,r,c):
    global answer
    if idx == d:
        if proper(showm):
            if not answer :
                answer = showm
            else:
                answer = sorted([answer,showm])[0]
        return
    for i in range(r,n):
        for j in range(c,n):
            if not showm[i][j]:
                showm[i][j] = idx
                solve(idx+1,showm,i,j)
                showm[i][j] = 0
                solve(idx,showm,i,j)

def proper(showm):
    for i in range(n):
        x_check = []
        for j in range(n):
            y_check = []
            if showm[i][j] and showm[i][j] not in x_check :
                x_check.append(showm[i][j])
            if showm[j][i] and showm[j][i] not in y_check:
                y_check.append(showm[j][i])
            if j == n-1:
                y_check.sort()
                if y_check!=check:
                    return False

        x_check.sort()
        if x_check != check:
            return False
    return True

    pass

n,d = map(int,input().split())
arr = [[0]*n for _ in range(n)]
check = [i for i in range(1,d)]
answer= list()
solve(1,arr,0,0)