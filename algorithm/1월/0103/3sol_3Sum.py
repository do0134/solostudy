# Leetcode 15. 3Sum
# https://leetcode.com/problems/3sum

from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        negative = list()
        positive = list()
        zeros = list()

        n = set()
        p = set()

        for num in nums:
            if num > 0:
                positive.append(num)
                p.add(num)
            elif num < 0:
                negative.append(num)
                n.add(num)
            else:
                zeros.append(num)

        answer = list()
        v = defaultdict(bool)

        if len(zeros) >= 3:
            answer.append([0, 0, 0])

        if zeros:
            for i in n:
                if -i in p and not v[(i, 0, -i)]:
                    answer.append([i, 0, -i])
                    v[(i, 0, -i)] = True

        for i in range(len(positive)):
            for j in range(i + 1, len(positive)):
                value = positive[i] + positive[j]
                if -value in n:
                    temp_key = tuple(sorted([-value, positive[i], positive[j]]))
                    if not v[temp_key]:
                        v[temp_key] = True
                        answer.append(temp_key)

        for i in range(len(negative)):
            for j in range(i + 1, len(negative)):
                value = negative[i] + negative[j]
                if -value in p:
                    temp_key = tuple(sorted([negative[i], negative[j], -value]))
                    if not v[temp_key]:
                        v[temp_key] = True
                        answer.append(temp_key)

        return answer