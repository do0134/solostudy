# Leetcode 561. Array Partition
# https://leetcode.com/problems/array-partition

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        answer = 0

        for i in range(0,len(nums),2):
            answer += nums[i]

        return answer