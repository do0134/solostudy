# 백준 1270 전쟁 - 땅따먹기

from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    my_dict = defaultdict(int)
    arr = list(map(int,input().split()))
    m = arr[0]

    answer = -1

    for i in range(1, m+1):
        my_dict[arr[i]] += 1
        if my_dict[arr[i]] > m // 2:
            answer = arr[i]
            break

    if answer == -1:
        print("SYJKGW")
    else:
        print(answer)