# Leetcode 77. Combinations
# https://leetcode.com/problems/combinations/description/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        num = [i for i in range(1,n+1)]

        answer = list()

        for i in combinations(num, k):
            answer.append(i)

        return answer