class Solution:

    

    def trap(self, height: List[int]) -> int:


        if not height:
            return 0
        total_water = 0
        max_left = 0
        max_right = 0

        l = 0
        r = len(height) - 1

        while l <= r:

            if max_left <= max_right:
                calculated_water = max_left - height[l]
                if calculated_water > 0:
                    total_water += calculated_water
                
                max_left = max(height[l], max_left)
                l += 1
                    
            else:
                calculated_water = max_right - height[r]
                if calculated_water > 0:
                    total_water += calculated_water
                
                max_right = max(height[r], max_right)

                r -= 1
        return total_water

            

            
                


