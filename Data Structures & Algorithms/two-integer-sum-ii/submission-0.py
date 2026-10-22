class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        while True:
            add = numbers[left] + numbers[right]
            if add == target:
                return [left+1,1+right]
            elif add < target:
                left+=1
            elif add > target:
                right -= 1