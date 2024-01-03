# 백준 16936 나3곱2

from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def back_tracking(num: int,answer_list: list,cnt: int):
    global v, flag
    if flag:
        return
    if cnt == n:
        flag = True
        print(*answer_list)
        return
    if not num % 3:
        value1 = num//3
        if v[value1]:
            v[value1] -= 1
            back_tracking(value1,answer_list + [value1],cnt+1)
            v[value1] += 1
    value2 = num*2
    if v[value2]:
        v[value2] -= 1
        back_tracking(value2, answer_list + [value2],cnt+1)
        v[value2] += 1


n = int(input())
arr = list(map(int,input().split()))
v = defaultdict(int)
for i in range(n):
    v[arr[i]] += 1

flag = False
for i in range(n):
    back_tracking(arr[i],[arr[i]],1)
    if flag:
        break

