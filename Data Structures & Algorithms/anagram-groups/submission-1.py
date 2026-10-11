class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        # for i in strs:
        #     freq = {}
        #     for char in i:
        #        freq[char] = freq.get(char,0) + 1
        #     key = tuple(sorted(freq.items()))
        #     if  key not in seen:
        #         seen[key] = [i]
        #     else:
        #         seen[key].append(i)
        # return list(seen.values())

        for i in strs:
            key =''.join(sorted(i))
            if key in seen:
                seen[key].append(i)
            else:
                seen[key]=[i]
        return list(seen.values())