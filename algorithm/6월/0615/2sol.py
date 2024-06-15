# 백준 8989 시계

import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    answer = list()
    arr = list(input().split())

    for i in arr:
        hour, min = i.split(":")
        hour, min = int(hour), int(min)
        if hour >= 12:
            hour -= 12
        x = (hour * 30) + (min * 0.5)
        y = min*6
        z = abs(x-y)
        while z > 180:
            z = abs(360-z)
        answer.append((z,i))

    answer.sort()
    print(answer[2][1])
