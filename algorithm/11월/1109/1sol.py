# 백준 15663 N과 M(9)

from itertools import permutations

n,m = map(int,input().split())
answer = set()
arr = list(map(int,input().split()))
for comb in permutations(arr, m):
    answer.add(comb)

answer = list(answer)
answer.sort()

for i in answer:
    print(*i)