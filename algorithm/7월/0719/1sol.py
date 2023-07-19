# 백준 16928 뱀과 사다리 게임
# https://www.acmicpc.net/problem/16928

from collections import defaultdict, deque

n,m = map(int,input().split())
ladder = defaultdict(int)
snake = defaultdict(int)

for _ in range(n):
    a,b = map(int,input().split())
    ladder[a] = b

for _ in range(m):
    a,b = map(int,input().split())
    ladder[a] = b

v = [int(1e9)]*101

q = deque()
q.append((1,0))

while q:
    cr, cnt = q.popleft()

    if cnt >= v[100]:
        continue

    for i in range(1,7):
        nr = i + cr
        if nr < 100 and v[nr] > cnt+1:
            if ladder[nr] and v[ladder[nr]] > cnt+1:
                q.append((ladder[nr],cnt+1))
                v[ladder[nr]] = cnt+1
                v[nr] = cnt+1
            elif snake[nr] and v[snake[nr]] > cnt+1:
                q.append((snake[nr],cnt+1))
                v[snake[nr]] = cnt+1
                v[nr] = cnt+1
            elif not snake[nr] and not ladder[nr]:
                q.append((nr,cnt+1))
                v[nr] = cnt+1
        elif nr >= 100 and v[100] > cnt+1:
            v[100] = cnt+1

print(v[100])