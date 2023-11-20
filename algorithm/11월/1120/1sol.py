# 백준 20040 사이클 게임

def find(x):
    if x != parent[x]:
        return find(parent[x])
    return x


def union(v1, v2):
    a = find(v1)
    b = find(v2)

    if a == b:
        return
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solve():
    global parent
    n, m = map(int, input().split())
    parent = [i for i in range(n)]

    for i in range(1,m+1):
        v1,v2 = map(int,input().split())
        if find(v1) == find(v2):
            return i
        union(v1, v2)
    return 0


print(solve())
