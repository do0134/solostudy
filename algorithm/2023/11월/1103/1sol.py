# 백준 1966 프린터큐

from collections import deque

t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    q = list(map(int,input().split()))
    q = deque(q)
    target = q[k]
    answer = 0

    important = [0]*10
    for i in q:
        important[i] += 1

    q[k] = -1
    while q:
        idx = q.popleft()
        flag = False
        next_idx = idx

        if idx == -1:
            next_idx = target

        for i in range(next_idx+1,10):
            if important[i]:
                q.append(idx)
                flag = True
                break

        if not flag:
            answer += 1
            if idx == -1:
                break
            important[idx] -= 1

    print(answer)
