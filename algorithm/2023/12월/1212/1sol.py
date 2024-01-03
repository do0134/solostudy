# 백준 2644 촌수계산

n = int(input())
a,b = map(int,input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
answer = -1

for _ in range(m):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

stack = list()

stack.append((a,0))
v = [0]*(n+1)
while stack:
    now,cnt = stack.pop()
    for next in arr[now]:
        if not v[next]:
            v[next] = cnt + 1
            stack.append((next, cnt+1))
    if v[b]:
        answer = v[b]
        break

print(answer)