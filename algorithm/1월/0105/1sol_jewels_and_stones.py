# Leetcode 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        type_dict = dict()

        for jewel in jewels:
            type_dict[ord(jewel)] = True

        answer = 0

        for stone in stones:
            if type_dict.get(ord(stone)):
                answer += 1

        return answer