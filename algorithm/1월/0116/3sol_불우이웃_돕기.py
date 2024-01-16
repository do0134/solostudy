# 백준 1414 불우이웃돕기

import sys
input = sys.stdin.readline


def make_num_dict():
    num_dict = dict()

    for _ in range(2):
        if not _:
            start = 97
            weight = 1
        else:
            start = 65
            weight = 27

        for i in range(26):
            num_dict[chr(start + i)] = weight + i

    return num_dict


def find(x):
    if x == parent[x]:
        return x

    return find(parent[x])


def union(x1, x2):
    a = find(x1)
    b = find(x2)

    if a == b:
        return

    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        rank[a] += 1


n = int(input())
rooms = [list(input().rstrip()) for _ in range(n)]
str_num_dict = make_num_dict()
str_num_dict["0"] = 0

vertex = list()
answer = 0

for i in range(n):
    for j in range(n):
        rooms[i][j] = str_num_dict[rooms[i][j]]
        w = rooms[i][j]
        answer += w
        if i == j :
            rooms[i][j] = 0
        elif rooms[i][j]:
            vertex.append((w,i,j))

vertex.sort()
parent = [i for i in range(n)]
rank = [0]*n
used = 0

for w,s,e in vertex:
    if find(s) != find(e):
        union(s,e)
        answer -= w
        used += 1
    if used == n-1:
        break
else:
    if used != n-1:
        answer = -1

print(answer)