# leetcode Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        appearance = list(set(arr))
        v = [0] * 1001

        for i in appearance:
            if v[arr.count(i)] == 1:
                return False
            v[arr.count(i)] += 1

        return True