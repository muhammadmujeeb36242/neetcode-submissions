class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        fixed = 0
        
        res = set()
        while fixed < len(nums)-2:
            seen = {}
            left = fixed + 1
            while left < len(nums):
                need = 0 - nums[fixed] - nums[left]
                if need in seen:
                    res.add(tuple(sorted([nums[fixed],nums[left],need])))
                else:
                    seen[nums[left]] = None
                left += 1
            fixed += 1
        return [list(triplet) for triplet in res]
            