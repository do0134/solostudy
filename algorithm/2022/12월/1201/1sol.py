# leet code 1704. Determine if String Halves Are Alike

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        s1 = s[0:len(s) // 2]
        s2 = s[len(s) // 2:len(s)]

        vowel = ["a", "e", "i", "o", "u"]

        cnt1 = 0
        cnt2 = 0

        for i in vowel:
            cnt1 += s1.count(i)
            cnt2 += s2.count(i)

        if cnt1 == cnt2:
            return True
        else:
            return False