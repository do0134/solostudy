# 1939 중량제한

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = dict()

for _ in range(m):
    s,e,w = map(int,input().split())
    if graph.get(s):
        if graph[s].get(e):
            if graph[s][e] < w:
                graph[s][e] = w
        else:
            graph[s][e] = w
    else:
        graph[s] = {e: w}

    if graph.get(e):
        if graph[e].get(s):
            if graph[e][s] < w:
                graph[e][s] = w
        else:
            graph[e][s] = w
    else:
        graph[e] = {s: w}

S, E = map(int,input().split())

"""
5 5
1 2 5
2 3 4
1 3 3
1 4 3
4 5 1
5 1
ans: 1

6 9
1 2 7
1 3 8
1 4 7
1 6 9
2 3 7
3 4 7
3 5 7
4 5 7
4 6 7
6 3
ans: 8

6 12
1 2 7
1 3 8
1 4 7
1 6 9
2 3 7
3 4 7
3 5 7
4 5 7
4 6 7
3 6 7
1 3 11
5 6 12
6 3
ans: 9

3 1
1 2 999999999
1 2
ans: 999999999

3 3
1 2 2
3 1 2
2 3 2
1 3
ans: 2

3 3
1 2 2
3 1 2
2 3 99999999
1 3
ans: 2

5 5
1 2 5
2 3 4
1 3 3
1 4 3
4 5 1
5 1
ans: 1
"""