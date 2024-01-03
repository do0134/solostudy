# Leetcode 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        answer_dict = defaultdict(list)
        answer_list = list()

        for s in strs:
            answer_dict["".join(sorted(s))].append(s)

        for key in answer_dict.keys():
            answer_list.append(answer_dict[key])

        return answer_list


