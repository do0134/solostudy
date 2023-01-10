#leetcode 1657. Determine if Two Strings Are Close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        char1 = sorted(set(word1))
        char2 = sorted(set(word2))
        if char1 != char2 :
            return False
        cnt1 = sorted(Counter(word1).values())
        cnt2 = sorted(Counter(word2).values())
        if cnt1 != cnt2 :
            return False
        return True