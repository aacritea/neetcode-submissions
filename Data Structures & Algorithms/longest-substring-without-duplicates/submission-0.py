class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        result = 0

        for r in range(len(s)):
            length = r - l + 1
            while s[r] in charSet:
                l += 1
            charSet.add(s[r])
            result = max(result, length)
        return result
