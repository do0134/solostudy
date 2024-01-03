# 백준 2252 줄세우기
# https://www.acmicpc.net/problem/2252

from collections import defaultdict
import sys

arr = list()
n,m = map(int,sys.stdin.readline().rstrip().split())
big_num = [0]*(n+1)
big = defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())
    big[a].append(b)
    big_num[b] += 1

for i in range(1,n+1):
    if not big_num[i]:
        arr += [i]

answer = list()
while arr:
    now_idx = arr.pop()
    answer.append(str(now_idx))
    for next_idx in big[now_idx]:
        big_num[next_idx] -= 1
        if not big_num[next_idx]:
            arr += [next_idx]

print(' '.join(answer))