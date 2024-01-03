# 백준 9466 텀 프로젝트


import sys

sys.setrecursionlimit(10**9)


def dfs(start):
    global v, answer, arr, visit

    next_idx = arr[start]
    visit.append(start)
    v[start] = 1

    if v[next_idx] and next_idx in visit:
        answer -= len(visit) - visit.index(next_idx)
        return

    elif not v[next_idx]:
        dfs(next_idx)


def solve():
    global v, answer, arr, visit
    input = sys.stdin.readline
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    answer = n
    v = [0]*(n+1)

    for i in range(1,n+1):
        if not v[i]:
            visit = list()
            v[i] = 1
            dfs(i)

    print(answer)


t = int(input())
for _ in range(t):
    solve()
