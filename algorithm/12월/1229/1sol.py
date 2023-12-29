# 백준 10773 제로

import sys
input = sys.stdin.readline

k = int(input())
stack = list()
for _ in range(k):
    n = int(input())
    if not n:
        stack.pop()
    else:
        stack.append(n)


print(sum(stack))