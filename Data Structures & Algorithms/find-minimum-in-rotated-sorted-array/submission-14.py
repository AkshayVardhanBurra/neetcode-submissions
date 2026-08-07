class Solution:
    def findMin(self, nums: List[int]) -> int:

        
        l = 0
        r = len(nums) - 1

        if(nums[l] <= nums[r]):
            return nums[l]
 

        while l <= r:


            mid = int((l + r)/2)

            if r - l == 1:
                return min(nums[r], nums[l])
            if nums[r] > nums[mid] and nums[l] > nums[mid]:
                #smallest number is in left half
                
                r = mid
                
            elif nums[r] < nums[mid] and nums[l] <= nums[mid]:
                #smallest number is in right half
                l = mid
            else:
                return nums[mid]
        return nums[l]

            
                
            


        