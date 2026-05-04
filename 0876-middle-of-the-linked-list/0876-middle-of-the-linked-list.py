# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        i=0
        while curr:
            curr=curr.next
            i+=1
        mid=i//2
        i=0
        while head:
            if(i==mid):
                return head
            head=head.next
            i+=1
        