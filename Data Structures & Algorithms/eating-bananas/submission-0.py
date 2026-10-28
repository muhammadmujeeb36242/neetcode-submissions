class Solution:
    from math import ceil
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower,upper = 1,max(piles)
        while lower < upper:
            new = (lower+upper)//2
            time = 0
            for pile in piles:
                time += (pile+new-1)//new
            if time <= h:
                upper = new
            else:
                lower = new + 1
        return lower