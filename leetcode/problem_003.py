'''
Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        used = {}
        max_length = start = 0
        for i, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
                
            used[char] = i
            
            print(used)
            print("start", start)
            print()

        return max_length

input = 'tmmzuxta'
S = Solution()
print(S.lengthOfLongestSubstring(input))

