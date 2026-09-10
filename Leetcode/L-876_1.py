# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def middleNode(self, head):
        curr = head
        curr1 = head
        x = 0

        while curr != None:
            x = x + 1
            curr = curr.next

        for i in range(x // 2):
            curr1 = curr1.next

        return curr1





        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        