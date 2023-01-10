from collections import deque

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    v = [0]*10001
    q = deque()
    v[a] = 1
    q.append((a,''))
    answer = ''
    while q:
        nv,fun = q.popleft()
        if nv == b:
            answer = fun
            break
        d = nv * 2
        if d > 9999:
            d = d % 10000

        s = nv - 1
        if s == -1:
            s = 9999

        l = (nv%1000*10) + (nv//1000)
        r = (nv%10*1000)+ (nv//10)
        if not v[d] :
            q.append((d,fun+'d'))
            v[d] = 1
        if not v[s] :
            q.append((s, fun+'s'))
            v[s] = 1
        if not v[l] :
            q.append((l, fun+'l'))
            v[l] = 1
        if not v[r] :
            q.append((r, fun+'r'))
            v[r] = 1

    print(answer.upper())


