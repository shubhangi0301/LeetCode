class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(target>nums[len(nums)-1]):
            return len(nums)
        if target<nums[0]:
            return 0
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = (low+high)//2
            if target<nums[mid]:
                high = mid-1
            elif target>nums[mid]:
                low = mid+1
            else:
                return mid
        return low
