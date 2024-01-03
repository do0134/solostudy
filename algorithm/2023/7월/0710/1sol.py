# 백준 13549 숨바꼭질 3
# https://www.acmicpc.net/problem/13549

from collections import deque

n, k = map(int,input().split())


def solve(n, k):
    q = deque()
    v = [int(1e9)]*min(200001, max(n,k)*2+1)
    l = len(v)
    q.append((n,0))
    v[n] = 0
    while q:
        idx, cnt = q.popleft()

        if idx > k:
            v[k] = min(v[k], idx - k + cnt)
            continue
        elif idx == k:
            v[idx] = min(v[k], cnt)
            continue
        if idx * 2 < l and v[idx*2] > cnt:
            q.append((idx*2,cnt))
            v[idx*2] = cnt
        if idx + 1 < l and v[idx+1] > cnt+1:
            q.append((idx+1,cnt+1))
            v[idx+1] = cnt+1
        if idx - 1 >= 0 and v[idx-1] > cnt+1:
            q.append((idx-1,cnt+1))
            v[idx-1] = cnt+1

    return v[k]


print(solve(n,k))