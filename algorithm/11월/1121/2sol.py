# 백준 9625 BABBA

k = int(input())


def solve(n):
    a = [0]*(n+1)
    b = [0]*(n+1)

    a[0] = 1

    for i in range(1,n+1):
        a[i] = b[i-1]
        b[i] = a[i-1] + b[i-1]

    return a[n], b[n]


print(*solve(k))