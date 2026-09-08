from collections import defaultdict

class Solution:


    #Will be at most O(26) since there are only 26 alphabets in the english language
    def checkReplacements(self, frequency_map):
        max_freq = 0

        for key,value in frequency_map.items():
            if value > max_freq:
                max_freq = value
        
        return max_freq
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        frequency_map = defaultdict(int)
        longest = 0

        for right in range(0, len(s)):
            
            frequency_map[s[right]] += 1

            most_occurred_char = self.checkReplacements(frequency_map)
            rang = right - left + 1
            if(rang - most_occurred_char > k):
                
                frequency_map[s[left]] -= 1
                left += 1
                longest = max(longest, right - left + 1)
                continue
            longest = max(longest, right - left + 1)


        return longest
                


        