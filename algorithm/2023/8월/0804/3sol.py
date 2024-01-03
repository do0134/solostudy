# softeer 징검다리
# https://softeer.ai/practice/info.do?idx=1&eid=390&sw_prbl_sbms_sn=236628
n = int(input())
arr = list(map(int,input().split()))

dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))