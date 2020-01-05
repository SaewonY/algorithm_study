class Solution:
    def lengthOfLongestSubstring(self, s):
        used = {}
        max_length = start = 0
        for i, char in enumerate(s):
            import pdb; pdb.set_trace()
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
                
            used[char] = i
        print(used)

        return max_length

input = 'abcabcbb'
S = Solution()
print(S.lengthOfLongestSubstring(input))

