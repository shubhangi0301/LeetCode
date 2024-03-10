class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(nums)-1
        k = j
        sorted_list = [0]*len(nums)
        while i<=j:
            if abs(nums[i])<=abs(nums[j]):
                sorted_list[k]=nums[j]*nums[j]
                j-=1
                k-=1
            elif abs(nums[i])>abs(nums[j]):
                sorted_list[k]=nums[i]*nums[i]
                i+=1
                k-=1
        return sorted_list

            

