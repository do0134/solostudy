# Leetcode 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

from collections import defaultdict
import heapq as hq


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # str_dict = defaultdict(int)
        # heap = list()
        answer = 0

        # for i in range(len(s)):
        #     char = s[i]

        #     if str_dict[char]:
        #         while heap and heap[0] <= str_dict[char]:
        #             idx = hq.heappop(heap)
        #             str_dict[idx] = 0
        #         str_dict[char] = i+1
        #         hq.heappush(heap,i+1)
        #     else:
        #         str_dict[char] = i+1
        #         hq.heappush(heap,i+1)

        #     answer = max(answer, len(heap))

        str_set = set()
        start = 0

        for i in range(len(s)):
            while s[i] in str_set:
                str_set.remove(s[start])
                start += 1
            str_set.add(s[i])
            answer = max(answer, i - start + 1)

        return answer