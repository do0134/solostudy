# leetcode 451. Sort Characters By Frequency
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        s_set = set(s)
        cnt = sorted(Counter(s).items(), key=lambda item: item[1], reverse=True)

        answer = ""
        for k, v in cnt:
            answer += k * v

        return answer