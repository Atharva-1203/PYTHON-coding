# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr=head
        count=0

        while(curr!=None):
            curr=curr.next
            count=count+1
        curr=head

        if n==count:
            return head.next
        curr=head
        
        for i in range(count-n-1):
            curr=curr.next
        curr.next=curr.next.next

        return head

        

        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
         