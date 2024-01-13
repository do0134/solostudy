# 백준 1647 도시 분할 계획
# https://www.acmicpc.net/problem/1647

import sys

input = sys.stdin.readline

n, m = map(int,input().split())
cities = list()

for _ in range(m):
    s,e,w = map(int,input().split())
    cities.append((w,s,e))

cities.sort()
parent = [i for i in range(n+1)]


def find(x):
    if x == parent[x]:
        return x

    return find(parent[x])


def union(a,b):
    x = find(a)
    y = find(b)

    if x < y:
        parent[x] = y
    else:
        parent[y] = x


answer = 0
delete_cost = 0

for cw, cs, ce in cities:
    if find(cs) != find(ce):
        union(cs, ce)
        answer += cw
        delete_cost = cw

print(answer-delete_cost)