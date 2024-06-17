# 백준 27396 문자열 변환과 쿼리

import sys

input = sys.stdin.readline

origin, n = input().split()
n = int(n)
v = [""]*123

for i in range(65, 123):
    v[i] = chr(i)

for _ in range(n):
    temp = input().rstrip()
    if len(temp) == 1:
        print(''.join(v[ord(char)] for char in origin))
    else:
        a, b, c = temp.split(" ")
        for i in range(65, 123):
            if v[i] == b:
                v[i] = c
