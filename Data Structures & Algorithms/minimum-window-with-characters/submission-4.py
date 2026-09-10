class Solution:

    #returns a map that is a frequency table of the string's characters
    def generateFrequencyTable(self, s):
        freq_table = {}

        for char in s:
            if char in freq_table:
                freq_table[char] += 1
            else:
                freq_table[char] = 1

        return freq_table




    def minWindow(self, s: str, t: str) -> str:
        s_dict = defaultdict(int)
        t_dict = self.generateFrequencyTable(t)
        less_eqs = 0
        left = 0
        
        result = ""
        for right in range(len(s)):
            s_dict[s[right]] += 1

            if s[right] in t_dict.keys() and t_dict[s[right]] == s_dict[s[right]]:
                less_eqs += 1
    
            
            while less_eqs == len(t_dict.keys()):
                if (result == "" or right - left + 1 < len(result)):
                    result = s[left:right + 1]
                    # print("writing result: " + result + " less eqs: " + str(less_eqs) + " left: " + str(left) + " right: " + str(right))
                
                if s_dict[s[left]] != 0:
                    s_dict[s[left]] -= 1
                if s[left] in t_dict.keys() and t_dict[s[left]] > s_dict[s[left]]:
                    # print("got here for: " + s[left])
                    less_eqs-=1
                left += 1
        return result
        



