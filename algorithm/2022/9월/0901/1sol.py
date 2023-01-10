from collections import deque as dq
def solve(S):
    if S[0] == 1:
        return 0
    else:
        K = S.pop(0)
        q = dq()
        cnt = 0
        v = list()
        for i in tree[S[0]]:
            if i in S:
                q.append((S[0],i))
        while q:
            cs, ce = q.popleft()

            for i in tree[ce]:
                if i in S:
                    pass
                





        return cnt


n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s,e = map(int,input().split())
    tree[s].append(e)
    tree[e].append(s)

q = int(input())

for _ in range(q):
    print(solve(list(map(int,input().split()))))


