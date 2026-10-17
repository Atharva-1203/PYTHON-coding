# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans=ListNode(-1)
        curr=ans
        t1=l1
        t2=l2
        carry=0

        while(t1 or t2):
            sum=carry
            if(t1):
                sum=sum+t1.val
            if(t2):
                sum=sum+t2.val
            temp=ListNode(sum%10)
            carry=sum/10

            curr.next=temp
            curr=curr.next

            if(t1):
                t1=t1.next
            if(t2):
                t2=t2.next
            
        if(carry):
            temp=ListNode(carry)
            curr.next=temp
            curr=curr.next

        return ans.next


        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        