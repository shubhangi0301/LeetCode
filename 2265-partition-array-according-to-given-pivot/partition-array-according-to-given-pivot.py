class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        less_arr = []
        grt_arr = []
        eq_arr = []
        for i in range(n):
            if(nums[i]<pivot):
                less_arr.append(nums[i])
            elif(nums[i]>pivot):
                grt_arr.append(nums[i])
            else:
                eq_arr.append(nums[i])
        less_arr.extend(eq_arr)
        less_arr.extend(grt_arr)
        return less_arr
        # for i in range(n):
        #     if(nums[i]<pivot):
        #         new_arr.append(nums[i])
        # for j in range(n):
        #     if(nums[j]==pivot):
        #         new_arr.append(nums[j])
        # for k in range(n):
        #     if(nums[k]>pivot):
        #         new_arr.append(nums[k])
        # return new_arr

