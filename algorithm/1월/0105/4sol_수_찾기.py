# 백준 1920 수찾기
# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

n = int(input())
arr = set(list(map(int,input().split())))

m = int(input())
target = list(map(int,input().split()))

for target_num in target:
    if target_num in arr:
        print(1)
    else:
        print(0)