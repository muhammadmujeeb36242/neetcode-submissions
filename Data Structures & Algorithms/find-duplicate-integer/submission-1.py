class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        seen = None
        for i in nums:
            if i == seen:
                return i
            else:
                seen = i