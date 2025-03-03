class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # i = 0
        # j = 0
        # n = len(nums)
        # new_arr = []
        # for k in range(n):
        #     if nums[k]<pivot:
        #         new_arr.append(nums[k])
        #         i+= 1
        #     elif nums[k]>pivot:
        #         new_arr.append(nums[k])
        #         j+= 1
        n = len(nums)
        new_arr = []
        for i in range(n):
            if(nums[i]<pivot):
                new_arr.append(nums[i])
        for j in range(n):
            if(nums[j]==pivot):
                new_arr.append(nums[j])
        for k in range(n):
            if(nums[k]>pivot):
                new_arr.append(nums[k])
        return new_arr

