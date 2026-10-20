class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        prefix = []
        for i in nums:
            prefix.append(pre)
            pre *= i
        suffix = []
        suff = 1
        for i in nums[::-1]:
            suffix.append(suff)
            suff *= i
        suffix.reverse()
        result = []
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])
        return result