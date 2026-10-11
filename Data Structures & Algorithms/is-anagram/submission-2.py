class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS,seenT = {},{}
        for i in s:
            if i in seenS:
                seenS[i] += 1
            else:
                seenS[i] = 0
        for i in t:
            if i in seenT:
                seenT[i] += 1
            else:
                seenT[i] = 0
        if seenS == seenT:
            return True
        else:
            return False