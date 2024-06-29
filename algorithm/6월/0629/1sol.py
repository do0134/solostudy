# 백준 31862 승리하라

import sys
from collections import defaultdict
input = sys.stdin.readline

n,m,k = map(int,input().split())
score = defaultdict(int)


cur_max = 0
k_arr = list()
arr = list()
answer = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    if not c:
        if a == k or b == k:
            k_arr.append((a,b))
        else:
            arr.append((a,b))
    elif c == 1:
        score[a] += 1
        cur_max = max(cur_max, score[a])
    else:
        score[b] += 1
        cur_max = max(cur_max, score[b])

if cur_max != score[k] and score[k] + len(k_arr) < cur_max:
    print(0)
else:
    poss = defaultdict(int)
    max_poss = score[k] + len(k_arr)
