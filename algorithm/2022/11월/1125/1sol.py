from collections import deque

n,m = map(int,input().split())

q = deque()

q.append((n,0))
v = [int(1e9)]*100001
if n == m :
    print(0)
else:
    while q :
        cr,cnt = q.popleft()

        f_v = cr + 1
        s_v = cr - 1
        t_v = cr*2

        if f_v < 100001 and v[f_v] > cnt + 1:
            q.append((f_v,cnt + 1))
            v[f_v] = cnt + 1

        if s_v > 0 and v[s_v] > cnt + 1 :
            q.append((s_v, cnt + 1))
            v[s_v] = cnt + 1

        if t_v < 100001 and v[t_v] > cnt + 1 :
            q.append((t_v, cnt+1))
            v[t_v] = cnt + 1

    print(v[m])