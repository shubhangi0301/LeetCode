class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst1 = []
        for num in nums:
            val = nums.count(num)
            lst1.append(val)
        max_num = max(lst1)
        count = 0
        for i in lst1:
            if i==max_num:
                count+= 1
        return count




        