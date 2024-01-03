# 백준 9095 1,2,3 더하기

def dfs(value):
    global answer

    if value > n:
        return
    elif value == n:
        answer += 1
        return
    else:
        for i in range(1,4):
            dfs(value+i)


t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    dfs(0)
    print(answer)