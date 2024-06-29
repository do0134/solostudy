# 백준 31862 승리하라
# 시간초과 계쏙남...

import sys
from collections import defaultdict
input = sys.stdin.readline

n,m,k = map(int,input().split())
score = defaultdict(int)
arr = list()
answer = 0
cnt = 0
v = defaultdict(bool)
for _ in range(m):
    a,b,c = map(int,input().split())
    if not c:
        arr.append((a,b))
    elif c == 1:
        score[a] += 1
    else:
        score[b] += 1


def brute(idx, max_v, now):
    global answer,cnt, v

    if v[now]:
        return

    v[now] = True
    cnt += 1

    if idx == len(arr):
        if check():
            answer += 1
        return

    if max_v - score[k] > len(arr) - idx:
        return

    a, b = arr[idx]
    score[a] += 1
    a_now = tuple(list(now) + [0])
    brute(idx+1, max(max_v, score[a]), a_now)
    score[a] -= 1
    b_now = tuple(list(now) + [1])
    score[b] += 1
    brute(idx+1, max(max_v, score[b]), b_now)
    score[b] -= 1


def check():
    max_v = 0
    first = 0
    flag = False
    for i in range(1,n+1):
        if max_v < score[i]:
            flag = False
            first = i
            max_v = score[i]
        elif max_v == score[i]:
            flag = True

    if not flag and first == k:
        return True

    return False


brute(0, max(score.values()), tuple())

print(answer)