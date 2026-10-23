class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if len(stack)!=0:
                p = stack[-1]+i
                if p=='()' or p=='[]' or p=='{}':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if len(stack)!=0:
            return False
        else:
            return True
