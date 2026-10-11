class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seenS={}
        for i in s:
            seenS[i] = seenS.get(i,0) + 1
        for i in t:
            if i not in seenS or seenS[i] == 0:
                return False
            else:
                seenS[i] -= 1
        return True