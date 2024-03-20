# 백준 1874 스택수열

import sys
input = sys.stdin.readline

n = int(input())
stack = list()
answer = list()

idx = 1

for _ in range(n):
    temp = int(input())

    if idx <= temp:
        while idx <= temp:
            stack.append(idx)
            idx += 1
            answer.append("+")

    if stack[-1] == temp:
        answer.append("-")
        stack.pop()
    else:
        answer = ["NO"]
        break

for i in answer:
    print(i)