class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        min_list = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        common_el = nums1.intersection(nums2)
        return min(common_el) if common_el else -1