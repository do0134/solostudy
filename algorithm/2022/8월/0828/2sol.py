def check():
    my_dict = {}
    for i in range(n):
        for j in range(n):
            if arr[i][j] :
                my_dict[arr[i][j]] = (i,j)
    return my_dict

def solve(idx,dist,r,c):
    global answer
    if idx == max_idx*2:
        answer = min(answer,dist)
        return
    for i in target.keys():
        if i < 0 :
            if -i in v and i not in v:
                v.append(i)
                solve(idx+1,dist+abs(target[i][0] - r) + abs(target[i][1] - c), target[i][0],target[i][1])
                v.pop()
        else:
            if i not in v:
                v.append(i)
                solve(idx+1,dist+abs(target[i][0] - r) + abs(target[i][1] - c), target[i][0],target[i][1])
                v.pop()




t = int(input())

for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    target = check()
    max_idx = max(target.keys())
    v= []
    answer = int(1e9)
    solve(0,0,0,0)
    print(f'#{tc} {answer}')