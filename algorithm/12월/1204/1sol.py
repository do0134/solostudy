# leetcode 2256. Minimum Average Difference

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        l_sum = 0

        if n == 1:
            return 0
        l = 1
        r = n - l
        min_v = int(1e9)
        answer = 0
        while r >= 0:
            l_sum += nums[l - 1]
            cl = l_sum // l
            if r != 0:
                cr = (total - l_sum) // r
            else:
                cr = 0

            if abs(cl - cr) < min_v:
                min_v = abs(cl - cr)
                answer = l - 1
                if min_v == 0:
                    return answer
            l += 1
            r -= 1

        return answer