# leetcode 198. House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 :
            return nums[0]
        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        def dfs(idx, n) :
            if idx+2 > n :
                return
            for i in range(idx+2, n) :
                if dp[idx]+nums[i] > dp[i] :
                    dp[i] = dp[idx] + nums[i]
                    dfs(i,n)
        
        dfs(0,n)
        dfs(1,n)
        return max(dp)
            
