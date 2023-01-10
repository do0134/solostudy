# leetcode 1962. Remove Stones to Minimize the Total

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        hq = [-i for i in piles]
        heapify(hq)
        
        for i in range(k) :
            temp = heappop(hq)
            heappush(hq,temp-int(temp/2))
        
        return -sum(hq)