from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # i = 0
        # j = n-1
        # for i in range(n):
        #     for j in range(i+1,n):   
        #         # if(nums[i]!=nums[j]):
        #         if(abs(i-j)<=k) and nums[i]==nums[j]:
        #             return True
        # return False
        # count_dict = {}
        # for i in range(n):
        #     if nums[i] not in count_dict:
        #         count_dict[nums[i]] = 1
        #     else:
        #         count_dict[nums[i]]+= 1 
        dict_map = {}
        for i in range(n):
            if nums[i] not in dict_map.keys():
                dict_map[nums[i]] = i
            else:
                if(abs(i-dict_map[nums[i]])<=k):
                    return True
                else:
                    dict_map[nums[i]] = i
        return False        