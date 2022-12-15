# leetcode 1143. Longest Common Subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        answer = 0

        for i in range(n1) :
            for j in range(n2) :
                if text1[i] == text2[j] :
                    dp[i+1][j+1] = dp[i][j] + 1
                else : 
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
                if dp[i+1][j+1] > answer :
                        answer = dp[i+1][j+1]
        return answer