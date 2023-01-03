# leetcode 944. Delete Columns to Make Sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        
        answer = 0
        for i in range(n) :
            temp = ""
            for j in strs : 
                temp += j[i]
            if list(temp) != sorted(list(temp)) :
                answer += 1

        return answer