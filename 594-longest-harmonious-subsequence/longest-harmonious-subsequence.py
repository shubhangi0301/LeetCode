from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        res = 0
        for x in nums_count.keys():
            if (x+1) in nums_count.keys():
                res = max(res,nums_count[x]+nums_count[x+1])
                # longest_sub  = nums_count[x]+nums_count[x+1]

        return res
