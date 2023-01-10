# leetcode 45. Jump Game II

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 :
            return 0
        v = [0]*n
        v[0] = -1
        
        q = deque()
        q.append((0,nums[0],0))
        
        while q :
            idx, jump, much = q.popleft()
            if jump == 0 :
                continue
            for i in range(idx+1,idx+jump+1) :
                if i < n and v[i] < much+1 :
                    if i == n-1 :
                        return much+1
                    q.append((i,nums[i],much+1))
                    v[i] = much+1