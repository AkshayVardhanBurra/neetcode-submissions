class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)
        left = 0
        long_long = 0
        char_set = set([])

        for right in range(0, len(s)):
            
            while s[right] in char_set:
                char_set.discard(s[left])
                left += 1
            
            char_set.add(s[right])
            gap = right - left + 1
            if gap > long_long:
                long_long = gap
        
        return long_long
        