class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket = [[]] * len(nums)
        # pre = None
        # count = 0
        # for i in nums:
        #     if i != pre:
        #         if i != nums[0]:
        #             bucket[count].append(i)
        #         count = 1
        #     else:
        #         count += 1

        # out = []
        # for i in bucket[::-1]:
        #     for j in i:
        #         out.append(j)
        #         k -= 1
        #         if k == 0:
        #             return out
        nums.sort()
        bucket = [[] for _ in range(len(nums)+1)]
        i = nums[0]
        count = 0
        for j in nums:
            if j == i:
                count += 1
            else:
                bucket[count].append(i)
                i = j
                count = 1
        bucket[count].append(i)

        result = []
        for i in bucket[::-1]:
            for j in i:
                result.append(j)
                k -= 1
                if k == 0:
                    return result