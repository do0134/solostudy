# 백준 1141 접두사
# https://www.acmicpc.net/problem/1141

n = int(input())
combi = set()

for i in range(n):
    s = input()

    if not combi:
        combi.add(s)
        continue

    for j in combi:
        if len(j) > len(s):
            if j[:len(s)] == s:
                break
        elif len(j) < len(s):
            if s[:len(j)] == j:
                combi.add(s)
                combi.discard(j)
                break
        elif j == s:
            break
    else:
        combi.add(s)

print(len(combi))