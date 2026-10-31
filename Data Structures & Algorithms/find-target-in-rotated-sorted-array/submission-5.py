class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0
        elif target > nums[0]:
            lower,upper = 0,nums.index(max(nums))
        else:
            lower,upper = nums.index(max(nums))+1, len(nums)-1
        while lower <= upper:
            nex = (lower+upper)//2
            if nums[nex] == target:
                return nex
            elif nums[nex] > target:
                upper = nex - 1
            else:
                lower = nex + 1
        return -1