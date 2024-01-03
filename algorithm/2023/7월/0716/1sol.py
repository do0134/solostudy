# 백준 18870 좌표 압축
# https://www.acmicpc.net/problem/18870

import sys
from collections import defaultdict

n = int(input())
idx = defaultdict(int)
arr = list(map(int, sys.stdin.readline().rstrip().split()))
for_idx = sorted(list(set(arr)))

num = 0
for i in for_idx:
    idx[i] = num
    num += 1

answer = list()
for i in arr:
    answer.append(idx[i])

print(*answer)