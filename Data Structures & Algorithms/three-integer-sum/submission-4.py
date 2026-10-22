class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # fixed = 0        
        # res = set()
        # while fixed < len(nums)-2:
        #     seen = {}
        #     left = fixed + 1
        #     while left < len(nums):
        #         need = 0 - nums[fixed] - nums[left]
        #         if need in seen:
        #             res.add(tuple(sorted([nums[fixed],nums[left],need])))
        #         else:
        #             seen[nums[left]] = None
        #         left += 1
        #     fixed += 1
        # return [list(triplet) for triplet in res]

        fixed = 0
        nums.sort()
        res = set()

        while fixed < len(nums)-2:
            # if fixed > 0 and nums[fixed] == nums[fixed-1]:
            #     fixed += 1
            #     continue

            l,r = fixed+1, len(nums)-1
            while l < r:
                total = nums[fixed] + nums[l] + nums[r]
                if total == 0:
                    res.add(tuple([nums[fixed],nums[l],nums[r]]))
                    l += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
            fixed += 1
        return [list(triplet) for triplet in res]