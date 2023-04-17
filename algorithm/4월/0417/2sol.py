# 백준 3584 가장 가까운 공통 조상
# https://www.acmicpc.net/problem/3584

from collections import defaultdict

t = int(input())
for _ in range(t) :
    n = int(input())
    tree = defaultdict(list)
    for _ in range(n-1) :
        s,e = map(int,input().split())
        tree[e].append(s)
    s1,s2 = map(int,input().split())
    v = [0] * (n+1)
    stack = list()
    stack.append((s1,s1))
    stack.append((s2,s2))
    v[s1] = s1
    v[s2] = s2
    while stack :
        now, root = stack.pop()
        for i in tree[now] :
            if v[i] != root and v[i] :
                print(i)
                stack = list()
                break
            elif not v[i] :
                stack.append((i,root))
                v[i] = root
            elif v[i] == root :
                continue
