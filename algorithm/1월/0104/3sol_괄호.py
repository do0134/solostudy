# 백준 9012 괄호
# https://www.acmicpc.net/source/42464325

T = int(input())

for _ in range(T):
    arr = list(input())
    cnt = 0
    for i in arr:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -=1
        if cnt < 0:
            print('NO')
            break
    else:
        if cnt :
            print('NO')
        else:
            print('YES')