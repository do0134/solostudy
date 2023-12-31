# 백준 12851 숨바꼭질 2

from collections import deque

n,k = map(int,input().split())

q = deque()
q.append((n,0))
v = [abs(i-n) for i in range(200001)]
v[n] = 0
if n == 1 or not n:
    cnt = 0
else:
    cnt = 1

if n == k:
    print(0)
    print(1)
elif n > k:
    print(n-k)
    print(1)
else:
    while q:
        c_idx, ct = q.popleft()
        if ct > v[k]:
            continue

        if c_idx > k:
            if c_idx-k+ct == v[k]:
                cnt += 1
            elif c_idx-k+ct < v[k]:
                cnt = 1
                v[k] = c_idx-k+ct
        else:
            if ct+1 <= v[2*c_idx]:
                if 2*c_idx == k:
                    if v[k] == ct+1:
                        cnt += 1
                    elif v[k] > ct+1:
                        cnt = 1
                        v[k] = ct+1
                else:
                    q.append((c_idx*2,ct+1))
                    v[2*c_idx] = ct+1
            if ct+1 <= v[c_idx+1]:
                if c_idx+1 == k:
                    if v[k] == ct + 1:
                        cnt += 1
                    elif v[k] > ct + 1:
                        cnt = 1
                        v[k] = ct + 1
                else:
                    q.append((c_idx+1,ct+1))
                    v[c_idx+1] = ct+1
            if ct+1 <= v[c_idx-1] and c_idx-1 >= 0:
                if c_idx-1 == k:
                    if v[k] == ct + 1:
                        cnt += 1
                    elif v[k] > ct + 1:
                        cnt = 1
                        v[k] = ct + 1
                else:
                    q.append((c_idx-1,ct+1))
                    v[c_idx-1] = ct+1

    print(v[k])
    print(cnt)
