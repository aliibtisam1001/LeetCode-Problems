# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr=head
        l=0
       
        while curr:
                curr=curr.next
                l+=1
        curr=head
        c=l-n
        i=1
        if c==0:
            head=curr.next
            return head
        while curr:
            if i==c:
                curr.next=curr.next.next
            curr=curr.next
            i+=1

        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna