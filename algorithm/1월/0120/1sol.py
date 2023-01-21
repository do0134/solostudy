# leetcode 491. Non-decreasing Subsequences
# https://leetcode.com/problems/non-decreasing-subsequences/description/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = list()

        for i in range(2,len(nums)+1) :
            for j in combinations(nums, i) :
                if list(j) == sorted(list(j)) and list(j) not in answer :
                    answer.append(list(j))
        return sorted(answer)

