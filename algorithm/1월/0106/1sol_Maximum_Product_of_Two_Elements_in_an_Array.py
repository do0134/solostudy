# Leetcode 1464. Maximum Product of Two Elements in an Array
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = list()

        for num in nums:
            heapq.heappush(heap, (-num))

        return (heapq.heappop(heap) + 1) * (heapq.heappop(heap) + 1)