# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.val==0 and head.next is None:
            return None
        sum = 0
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        dict_sum = {}
        while temp is not None:
            sum+=temp.val
            dict_sum[sum] = temp
            temp = temp.next
        sum = 0
        temp = dummy
        while temp is not None:
            sum+=temp.val
            temp.next = dict_sum[sum].next
            temp = temp.next
        return dummy.next