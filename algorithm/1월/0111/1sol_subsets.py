# Leetcode 78. Subsets
# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = list()

        for i in range(len(nums) + 1):
            for combi in combinations(nums, i):
                answer.append(combi)

        return answer