class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if(nums[i]==nums[i+1]):
                nums[i] = nums[i]*2
                nums[i+1] = 0
        
        p = 0
        for q in range(n):
            if nums[q]!=0:
                nums[p] = nums[q]
                p+= 1
        for k in range(p,n):
            nums[p] = 0
            p+= 1

        # q = 1
        # while(p<n-1):
        #     if(nums[p]==0):
        #     # p+= 1
        #     # q+=1
        #         temp = nums[p]
        #         nums[p] = nums[q]
        #         nums[q] = temp
        #     p+=1
        #     q+=1

        return nums

        # for j in range(n):
        #     if nums[j]==0:
        #         nums
