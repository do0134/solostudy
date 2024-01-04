# Leetcode 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = list()
        answer = [0]*n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                answer[idx] = i-idx
            stack.append(i)

        return answer