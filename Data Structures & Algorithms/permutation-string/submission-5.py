class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        char_dict = defaultdict(int)
        check_dict = defaultdict(int)

        for char in s1:
            check_dict[char] += 1

        for right in range(0,len(s2)):

            char_dict[s2[right]] += 1

            if right - left + 1 > len(s1):
                # print(f"left: {left}, right: {right}")
                # print(char_dict)
                print(f"doing char_dict[{s2[left]}] -= 1 -> {char_dict[s2[left]] - 1}) original {char_dict[s2[left]]}")
                char_dict[s2[left]] -= 1
                left += 1
     
         
            found = 0
            for char_key in check_dict.keys():
                if char_dict[char_key] == check_dict[char_key]:
                    found += 1

            
            if found == len(check_dict):
                return True
        
        return False
                

