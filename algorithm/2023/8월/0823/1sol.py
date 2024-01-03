# 백준 28279 덱2

from collections import deque
import sys
n = int(input())
dq = deque()

for _ in range(n):
    fun = list(map(int,sys.stdin.readline().split()))
    if fun[0] == 1:
        dq.appendleft(fun[1])
    elif fun[0] == 2:
        dq.append(fun[1])
    elif fun[0] == 3:
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif fun[0] == 4:
        if not dq:
            print(-1)
        else:
            print(dq.pop())
    elif fun[0] == 5:
        print(len(dq))
    elif fun[0] == 6:
        if not dq:
            print(1)
        else:
            print(0)
    elif fun[0] == 7:
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif fun[0] == 8:
        if not dq:
            print(-1)
        else:
            print(dq[-1])
