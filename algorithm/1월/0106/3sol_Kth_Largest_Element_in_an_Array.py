# Leetcode 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        cnt = 0

        while cnt < k:
            now = heapq.heappop(nums)
            cnt += 1

        return -now