# 백준 16974 레벨 햄버거

n,x = map(int,input().split())


def made_burger():
    patty = [0]*(n+1)
    patty[0] = 1
    burger = [0]*(n+1)
    burger[0] = 1

    for i in range(1,n+1):
        patty[i] = patty[i-1]*2+1
        burger[i] = burger[i-1]*2+3

    return patty, burger


patty, burger = made_burger()


def d_n_c(level, cnt):
    if level == 0:
        return cnt
    elif cnt == 1:
        return 0
    elif cnt <= 1+burger[level-1]:
        return d_n_c(level-1, cnt-1)
    elif cnt == 2 + burger[level-1]:
        return patty[level-1]+1
    elif cnt <= burger[level-1]*2+2:
        return patty[level-1]+1+d_n_c(level-1, cnt-(burger[level-1]+2))
    else:
        return patty[level]


print(d_n_c(n,x))