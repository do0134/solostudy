# Leetcode 77. Combinations
# https://leetcode.com/problems/combinations/description/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        global answer

        answer = list()

        nums = [i for i in range(1, n + 1)]

        # for i in combinations(nums, k):
        #     answer.append(i)

        def back_tracking(nums, combi, idx):
            global answer
            if len(combi) == k:
                answer.append(combi[:])
                return
            elif len(combi) + len(nums) - idx < k:
                return

            for i in range(idx + 1, len(nums)):
                back_tracking(nums, combi + [nums[i]], i)

        back_tracking(nums, [], -1)

        return answer