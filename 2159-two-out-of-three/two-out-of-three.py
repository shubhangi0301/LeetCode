class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        arr = []
        nums1 = set(nums1) #1,3,2
        nums2 = set(nums2) #2,3
        nums3 = set(nums3) #3
        
        z = (nums1 & nums2) | (nums2 & nums3) | (nums1 & nums3)
            #2,3                #3              #3
        #2,3
        return list(z)
        # for i in nums1:
        #     arr_dict[i] =  1
        # for j in nums2:
        #     if j not in nums1:
        #         arr_dict[j] = 1
        
