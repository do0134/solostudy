# 백준 2660 회장뽑기
# https://www.acmicpc.net/problem/2660

from collections import deque, defaultdict

def bfs(start):
    q = deque()
    q.append((start,0))

    while q:
        idx, cnt = q.popleft()
        for j in people[idx]:
            if not tree[start][j] or tree[start][j] > cnt + 1:
                tree[start][j] = cnt + 1
                q.append((j, cnt + 1))

    tree[start][start] = 0
    return max(tree[start])


n = int(input())
people = defaultdict(list)
point = defaultdict(int)
tree = [[0]*(n+1) for _ in range(n+1)]

while True:
    a, b = map(int,input().split())
    if a == b and b == -1:
        break
    people[a].append(b)
    people[b].append(a)

max_v = int(1e9)
answer = list()
for i in range(1,n+1):
    point[i] = bfs(i)
    if point[i] == max_v:
        answer.append(i)
    elif point[i] < max_v:
        max_v = point[i]
        answer = [i]

print(max_v,len(answer))
print(*answer)
