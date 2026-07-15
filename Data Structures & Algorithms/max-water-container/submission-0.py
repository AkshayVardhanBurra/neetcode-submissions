class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights) - 1
        max_water = 0
        while i < j:
            
            calculated_water = (j - i) * min(heights[i], heights[j])

            if calculated_water > max_water:
                max_water = calculated_water
            if heights[i] < heights[j]:
                i += 1

            else:
                j-=1
        
        return max_water