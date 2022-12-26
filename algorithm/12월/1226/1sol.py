# leetcode 55. Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1 :
            return True
        v = [0]*n
        v[0] = 1
        
        for i in range(n) :
            if not v[i] :
                continue
            if i+nums[i] >= n-1 :
                return True 
            for j in range(i+1,i+nums[i]+1) :
                if j >= n : 
                    break
                v[j] = 1
        return False