# Leetcode 198. House Robber
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if n == 1:
            return nums[0]

        dp[0] = nums[0]

        for i in range(n - 1):
            dp[i + 1] = max(dp[i], nums[i + 1] + dp[i - 1])

        return max(dp)