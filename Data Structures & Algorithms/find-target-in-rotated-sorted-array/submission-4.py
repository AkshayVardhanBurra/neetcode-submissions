class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            if nums[l] <= nums[r]:

                mid = (l + r) // 2

                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    return mid
            else:
                
                mid = (l + r) // 2
                # check if we are in left sorted or right sorted portions

                #right sorted portion
                if target == nums[mid]:
                    return mid
                if nums[mid] < nums[l]:
                    if target < nums[mid]:
                        #in left half
                        r = mid - 1
                    elif target > nums[mid] and target <= nums[r]:
                        l = mid + 1
                    elif target > nums[mid] and target > nums[r]:
                        r = mid - 1
                elif nums[mid] >= nums[l]:
                    # target is in right half
                    if target > nums[mid]:
                        l = mid + 1
                    elif target < nums[mid] and target < nums[l]:
                        l = mid + 1
                    elif target < nums[mid] and target >= nums[l]:
                        r = mid - 1
                

                    

        return -1