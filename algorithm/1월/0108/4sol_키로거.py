# 백준 5397 키로거

from collections import deque

def solve(s):
    left = deque()
    right = deque()

    for i in s:
        if i == "<":
            if left:
                val = left.pop()
                right.appendleft(val)
        elif i == ">":
            if right:
                val = right.popleft()
                left.append(val)
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)

    return list(left+right)


n = int(input())

for _ in range(n):
    s = list(input())
    print("".join(solve(s)))