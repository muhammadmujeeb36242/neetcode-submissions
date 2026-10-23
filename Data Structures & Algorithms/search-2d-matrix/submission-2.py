class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binsearch(nums,target):
            l,r = 0,len(nums)-1
            if nums[l]==target:
                return True
            elif nums[r]==target:
                return True
            else:
                while r>l+1:
                    if nums[l]!=target and nums[r]!=target:
                        m = (l+r)//2
                        if nums[m] > target:
                            r = m
                        elif nums[m] < target:
                            l = m
                        else:
                            return True
                    elif nums[l] == target:
                        return True
                    else:
                        return True 
            return False
        row = None
        for Row in matrix:
            if Row[0] <= target <= Row[-1]:
                row = Row
        if row!=None:
            return binsearch(row,target)
        else:
            return False
        