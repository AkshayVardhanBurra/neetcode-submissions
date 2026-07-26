class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bwise = 0
        for num in nums:
            one = 1 << num

            if bwise & one:
            
                return num
            else:
               
                bwise |= one
        
            
        
        return 0
        