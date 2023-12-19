# 백준 11055 가장 큰 중가하는 부분 수열

n = int(input())
arr = list(map(int,input().split()))
dp = [0]*n
dp[0] = arr[0]

for i in range(n):
    for j in range(i+1,n):
        if arr[i] < arr[j]:
            dp[j] = max(dp[i]+arr[j],dp[j])
        elif arr[i] >= arr[j] and not dp[j]:
            dp[j] = arr[j]

print(max(dp))