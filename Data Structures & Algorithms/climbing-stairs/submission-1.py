class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,1,2]
        if n == 1:
            return 1
        elif n ==2:
            return 2
        for i in range(3,n+1):
            step = steps[i-1]+steps[i-2]
            steps.append(step)
        return step