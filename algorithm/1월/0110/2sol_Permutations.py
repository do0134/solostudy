# Leetcode 46. Permutations
# https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = list()

        for i in permutations(nums, len(nums)):
            answer.append(i)

        return answer