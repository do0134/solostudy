t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*n for i in range(2)]
    if n == 1:
        max_v = max(arr[0][0],arr[1][0])
    elif n == 2:
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[1][1] + arr[0][0]
        max_v = max(dp[0][1],dp[1][1])
        pass
    elif n > 3:
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        dp[0][1] = arr[1][0]+arr[0][1]
        dp[1][1] = arr[1][1]+arr[0][0]
        max_v = 0
        for i in range(2,n):
            dp[0][i] = max((dp[1][i-1]+arr[0][i]),(dp[0][i-2]+arr[0][i]),(dp[1][i-2]+arr[0][i]))
            dp[1][i] = max((dp[0][i-1]+arr[1][i]),(dp[1][i-2]+arr[1][i]),(dp[0][i-2]+arr[1][i]))
            max_v = max(max_v,dp[0][i],dp[1][i])
    print(max_v)
