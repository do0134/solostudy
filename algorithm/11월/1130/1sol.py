# 백준 4803 트리

from collections import deque


def bfs(start, v):
    q = deque()
    q.append((start, -1))
    v[start] = 1
    flag = True

    while q:
        now, parent = q.popleft()
        for next_idx in graph[now]:
            if next_idx != parent:

                if v[next_idx]:
                    return False
                else:
                    q.append((next_idx, now))
                    v[next_idx] = 1
    return flag


tc = 1

while True:
    n,m = map(int,input().split())
    if not n and not m:
        break
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)

    answer = 0
    v = [0]*(n+1)
    for i in range(1,n+1):
        if not v[i]:
            if bfs(i,v):
                answer += 1

    if not answer:
        s = "No trees."
    elif answer == 1:
        s = "There is one tree."
    else:
        s = f"A forest of {answer} trees."
    print(f"Case {tc}: {s}")
    tc += 1

"""
6 6
1 2
2 3
4 5
5 6
4 6
3 4
0 0
"""