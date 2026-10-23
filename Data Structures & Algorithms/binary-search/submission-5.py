class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        nums.sort()
        if nums[l]==target:
            return l
        elif nums[r]==target:
            return r
        else:
            while r>l+1:
                if nums[l]!=target and nums[r]!=target:
                    m = (l+r)//2
                    if nums[m] > target:
                        r = m
                    elif nums[m] < target:
                        l = m
                    else:
                        return m
                elif nums[l] == target:
                    return l
                else:
                    return r
        return -1