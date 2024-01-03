#  백준 11724 연결 요소의 개수

from collections import defaultdict, deque

n,m = map(int,input().split())
v = [0]*(n+1)
tree = defaultdict(list)

for _ in range(m):
    s,e = map(int,input().split())
    tree[s].append(e)
    tree[e].append(s)

answer = 0
for i in range(1,n+1):
    if not v[i]:
        q = deque()
        q.append(i)
        v[i] = 1
        answer += 1
        while q:
            idx = q.popleft()
            for next_idx in tree[idx]:
                if not v[next_idx]:
                    v[next_idx] = 1
                    q.append(next_idx)

print(answer)