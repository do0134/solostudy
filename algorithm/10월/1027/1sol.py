from collections import deque

n = int(input())
arr = list(map(int,input().split()))
dp = [int(1e9)] * n

q= deque()
q.append((0,0))

while q :
    ci,cd = q.popleft()
    print(ci,cd)
    ni = ci + arr[ci]
    if ni >= n-1 :
        ni = n-1
    for i in range(ci, ni+1):
        if dp[i] > cd + 1:
            dp[i] = cd+1
            q.append((ni,dp[i]))
if dp[-1] == int(1e9):
    print(-1)
else:
    print(dp[-1])

