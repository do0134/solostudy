from collections import defaultdict


def check(cidx,nidx,ccx,ccy,nnx,nny):
    max_x = max(ccx,nnx)
    max_y = max(ccy,nny)
    min_x = min(ccx,nnx)
    min_y = min(ccy,nny)
    flag = [0]*(k+1)

    for i in range(1,k+1):
        if i == cidx or i == nidx:
            flag[i] = 1
            continue
        for r,c in color[i]:
            print(i,r,c,min_x,max_x,min_y,max_y)
            if min_x <= r <= max_x and min_y <= c <= max_y:
                print(r,c)
                flag[i] = 1
                break
    for i in range(1,k+1):
        if not flag[i]:
            return False
    return True


n, k = map(int,input().split())
color = defaultdict(list)

for _ in range(n):
    x,y,c = map(int,input().split())
    color[c].append((x,y))

answer = int(1e9)

for i_idx in range(1,k+1):
    for cx,cy in color[i_idx]:
        for j_idx in range(i_idx+1,k+1):
            for nx,ny in color[j_idx]:
                if check(i_idx,j_idx,cx,cy,nx,ny):
                    print(i_idx,j_idx)
                    answer = min(answer, (max(cx,nx)-min(cx,nx))*(max(cy,ny)-min(cy,ny)))

print(answer)

