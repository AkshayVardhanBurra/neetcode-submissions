class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)
        left = 0
        longest_sub = 0
        long_long = 0
        char_set = set([])

        for right in range(0, len(s)):
            
            longest_sub += 1

            while s[right] in char_set:
                longest_sub -= 1
                char_set.discard(s[left])
                left += 1
            
            char_set.add(s[right])
            if longest_sub > long_long:
                long_long = longest_sub
        
        return long_long
        