# 백준 1188 음식평론가


def gcd(x,y):
    if not y:
        return x
    return gcd(y,x%y)


def solve():
    n,m = map(int,input().split())
    print(m - gcd(n,m))


solve()