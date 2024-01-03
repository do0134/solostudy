# 백준 20922 겹치는건 싫어

from collections import defaultdict

n,k = map(int,input().split())
arr = list(map(int,input().split()))

cnt = defaultdict(int)

l = 0
r = 1

cnt[arr[l]] += 1
answer = 1
length = 1
while r < n:
    answer = max(answer, length)
    cnt[arr[r]] += 1
    if cnt[arr[r]] > k:
        while cnt[arr[r]] > k and l < r:
            cnt[arr[l]] -= 1
            l += 1
            length -= 1
    r += 1
    length += 1

answer = max(answer, length)

print(answer)