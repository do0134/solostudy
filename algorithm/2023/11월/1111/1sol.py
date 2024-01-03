# 백준 27172 수 나누기 게임

from collections import defaultdict

n = int(input())
arr = list(map(int,input().split()))

answer = [0]*n

num = defaultdict(bool)
idx = defaultdict(int)

for i in range(n):
    num[arr[i]] = True
    idx[arr[i]] = i

m = max(arr)+1
for i in range(n):
    for j in range(2*arr[i], m, arr[i]):
        if num[j]:
            answer[i] += 1
            answer[idx[j]] -= 1

print(*answer)