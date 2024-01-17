# 백준 5052 전화번호 목록

import sys
input = sys.stdin.readline


def solve(arr):
    set_arr = set(arr)

    if len(arr) != len(set_arr):
        return "NO"

    arr.sort(key=lambda x:len(x))
    for i in arr:
        if len(i) == len(arr[0]):
            continue
        for j in range(len(arr[0])-1,len(i)):
            if i[:j] in set_arr:
                return "NO"

    return "YES"


t = int(input())

for _ in range(t):
    n = int(input())
    temp = list()
    for _ in range(n):
        temp.append(input().rstrip())

    print(solve(temp))