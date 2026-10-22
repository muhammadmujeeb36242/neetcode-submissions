class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        res = 0
        while l<r:
            limit = min(heights[l],heights[r])
            water = (r-l)*limit
            res = max(res,water)
            if limit == heights[l]:
                l += 1
            elif limit == heights[r]:
                r -= 1
        return res