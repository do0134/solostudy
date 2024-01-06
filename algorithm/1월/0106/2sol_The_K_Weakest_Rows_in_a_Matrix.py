# Leetcode 1337. The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = list()

        for idx, line in enumerate(mat):
            heapq.heappush(heap, (line.count(1), idx))

        answer = list()

        while heap:
            answer.append(heapq.heappop(heap)[1])
            if len(answer) == k:
                break

        return answer
