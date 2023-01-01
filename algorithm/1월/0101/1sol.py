# leetcode 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        my_dict = defaultdict(str)
        second_dict = defaultdict(str)
        s = list(s.split())
        n = len(pattern)
        if len(s)%n != 0 :
            return False
        for i in range(n) :
            if my_dict[pattern[i]] == s[i] and second_dict[s[i]] == pattern[i]:
                continue
            elif not my_dict[pattern[i]] and not second_dict[s[i]]:
                my_dict[pattern[i]] = s[i]
                second_dict[s[i]] = pattern[i]
            else : 
                return False
            
        return True