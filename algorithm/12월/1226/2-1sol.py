# leetcode 45. Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 :
            return 0
        
        l = 0 
        r = 0
        answer = 0

        while r < n-1 :
            d = 0
            for i in range(l,r+1) :
                d = max(d,i+nums[i])
            l = r+1
            r = d
            answer += 1
        
        return answer