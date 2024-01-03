# 백준 2116 주사위 쌓기
# https://www.acmicpc.net/problem/2116

from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)

next_floor = {"A" : "F", "B" : "D", "C" : "E", "D" : "B", "E" : "C", "F" : "A"}


def brute_force(idx, start, end, cnt):
    global answer
    if idx == n+1:
        answer = max(answer, cnt)
        return

    value = 0
    
    for s in "ABCDEF":
        if s != start and s != end:
            value = max(value,dice[idx][s])

    if idx < n:
        for next_s in "ABCDEF":
            if dice[idx+1][next_s] == dice[idx][end]:
                start = next_s
                end = next_floor[next_s]
                break

    brute_force(idx+1, start, end, cnt+value)


n = int(input())
dice = defaultdict(defaultdict)

for i in range(n):
    temp_arr = list(map(int, input().split()))
    for temp_idx, s in zip(temp_arr, "ABCDEF"):
        dice[i+1][s] = temp_idx

answer = 0

for s in "ABCDEF":
    brute_force(1,s,next_floor[s],0)

print(answer)