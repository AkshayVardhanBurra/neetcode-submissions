import math
class Solution:

    def test_list(self, piles, rate):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/rate)
        return hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        right = max(piles)
        left = 1
        last_mid = right

        while left <= right:
            mid = int((left + right)/2)

            if self.test_list(piles, mid) <= h:
                right = mid - 1
                last_mid = mid
            else:
                left = mid + 1
        return last_mid
            


    
        