# Leetcode 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_palindrom(s: str, l: int, r: int) -> bool:
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1

            if l == r or l > r:
                return True

            return False

        n = len(s)
        max_len = 1
        answer = [0, 0]

        for i in range(n):
            if n - 1 - i < max_len:
                break
            j = i + max_len
            while j < n:
                if max_len > j - i + 1:
                    j = i + max_len
                if find_palindrom(s, i, j):
                    if max_len < j - i + 1:
                        max_len = j - i + 1
                        answer = [i, j]
                j += 1

        return s[answer[0]:answer[1] + 1]