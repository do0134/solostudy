# leetcode 2279. Maximum Bags With Full Capacity of Rocks

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        diff = [0]*n
        s = 0
        z_cnt = 0
        for i in range(n) :
            diff[i] = capacity[i] - rocks[i]
            s += diff[i]
            if diff[i] == 0 :
                z_cnt += 1

        if s == 0 or s < additionalRocks : 
            return n 
        
        diff.sort()
        cnt = additionalRocks
        
        for i in range(n) :
            if cnt < diff[i] or cnt == 0:
                break
            if diff[i] == 0 :
                continue
            cnt -= diff[i]
            diff[i] = 0
            z_cnt += 1

        return z_cnt