# 백준 2751 수 정렬하기 2

import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    arr.append(int(input()))

arr.sort()

for i in arr:
    print(i)