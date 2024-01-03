# 백준 아레나 A번 내 집 마련하기

from collections import defaultdict

n = int(input())
answer = defaultdict(list)
idx = defaultdict(int)
arr = list(map(int,input().split()))

m = int(input())
for i in range(n):
    idx[i] = arr[i]

for _ in range(m):
    l,r = map(int,input().split())
    if answer[(l,r)]:
        print(*answer[(l,r)])
        continue

    temp1 = list()
    for i in range(n):
        if l <= idx[i] <= r:
            temp1.append(idx[i])

    temp1.sort(reverse=True)
    temp = list()
    for i in range(n):
        if l <= idx[i] <= r:
            temp.append(temp1.pop())
        else:
            temp.append(idx[i])

    answer[(l,r)] = temp
    print(*temp)