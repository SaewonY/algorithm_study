'''
Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def helper(i, j):
            while i >=0 and j < len(s) and s[i]==s[j]:
                i -= 1
                j += 1
            return s[i+1:j]  # s[i] != s[j]

        return s and max((a for i in range(len(s)) 
                          for a in (helper(i, i), helper(i, i+1))), key=len) or ''
            

input = "babad"
A = Solution()
print(A.longestPalindrome(input))