# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        curr=head
        if(curr==None or curr.next==None):
            return head

        while(curr!=None and curr.next!=None):
            if(curr.val==curr.next.val):
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        