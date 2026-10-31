class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        res.append([])
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                start = prev_start
            else:
                start = 0
            prev_start = len(res)   
            for j in range(start,prev_start):
                res.append(res[j]+[nums[i]])
        return res