# Leetcode 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1

        keys = sorted(num_dict.keys(), key=lambda x : num_dict[x], reverse= True)

        return keys[:k]