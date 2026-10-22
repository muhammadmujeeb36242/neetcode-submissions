class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(s1))
        left = 0
        
        for right in range(len(s1),len(s2)+1):
            sub = ''.join(sorted(s2[left:right]))
            if sub == s1:
                return True
            else:
                left += 1
        return False