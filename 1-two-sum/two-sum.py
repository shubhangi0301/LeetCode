class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        for i in range(len(nums)):
            while start<end:
                if((nums[start]+nums[end])==target):
                    return start,end
                else:
                    end-=1
            start+=1
            end = len(nums)-1
        return start,end
        