# 백준 1099 알 수 없는 문장
# https://www.acmicpc.net/problem/1099

import sys
from collections import defaultdict


def check(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    return sorted(s1) == sorted(s2)


def make_point(s1,s2):
    value = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            value += 1
    return value


target = input()
n = int(input())
words = defaultdict(list)

for _ in range(n):
    temp = sys.stdin.readline().rstrip()
    words[len(temp)].append(temp)

dp = [[int(1e9)]*(len(target)+1) for i in range(len(target)+1)]
dp[0][0] = 0

for i in range(len(target)+1):
    if dp[i][0] == int(1e9) and i:
        continue
    for j in range(1, len(target)-i+1):
        for word in words[j]:
            if check(target[i:i+j], word):
                point = make_point(target[i:i+j], word)
                if i :
                    dp[i][i+j] = min(dp[i][i+j], dp[i][0]+point)
                else:
                    dp[i][i+j] = point
                dp[i+j][0] = min(dp[i+j][0],dp[i][i+j])


if dp[-1][0] == int(1e9):
    print(-1)
else:
    print(dp[-1][0])