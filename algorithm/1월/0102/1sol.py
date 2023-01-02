# leetcode 520. Detect Capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word : 
            return 1
        elif word.lower() == word : 
            return 1
        elif word[0].upper()+word[1:].lower() == word : 
            return 1

        return 0