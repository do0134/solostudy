# leetcode 931. Minimum Falling Path Sum

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[int(1e9)]*n for _ in range(n)]
        
        for i in range(n) :
            dp[0][i] = matrix[0][i]
        
        for i in range(1,n) :
            for j in range(n) :
                if j-1 >= 0 :
                    dp[i][j-1] = min(dp[i][j-1],dp[i-1][j]+matrix[i][j-1])
                if j+1 < n :
                    dp[i][j+1] = min(dp[i][j+1],dp[i-1][j]+matrix[i][j+1])
                dp[i][j] = min(dp[i][j],dp[i-1][j]+matrix[i][j]) 


        return min(dp[n-1])