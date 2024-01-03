# Leetcode 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict


class Solution:
    def __init__(self):
        self.answer_dict = defaultdict(list)
        self.answer_list = list()

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for s in strs:
            self.answer_dict["".join(sorted(s))].append(s)

        for key in self.answer_dict.keys():
            self.answer_list.append(self.answer_dict[key])

        return self.answer_list
