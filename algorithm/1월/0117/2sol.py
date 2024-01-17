# 백준 10814 나이순 정렬

import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for i in range(n):
    age, name = input().split()
    age = int(age)
    arr.append((age,i,name))

arr.sort()

for age, idx, name in arr:
    print(age, name)