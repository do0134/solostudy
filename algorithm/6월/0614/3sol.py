# 백준 18018 Alphabet Animals

import sys
from collections import defaultdict

input = sys.stdin.readline

start = input().rstrip()
n = int(input())


def solve(start, n):
    str_dict = defaultdict(list)
    first = ""
    for _ in range(n):
        temp = input().rstrip()
        if temp[0] == start[-1] and not first:
            first = temp
        str_dict[temp[0]].append(temp)

    if not first:
        return "?"

    for i in str_dict[start[-1]]:
        if not str_dict[i[-1]] or (len(str_dict[i[-1]]) == 1 and str_dict[i[-1]][0] == i):
            return i+"!"

    return first


print(solve(start,n))