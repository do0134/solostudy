# leetcode 2389. Longest Subsequence With Limited Sum

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        target = list(accumulate(sorted(nums)))
        answer = list()
        for query in queries :
            answer.append(bisect_right(target,query))

        return answer