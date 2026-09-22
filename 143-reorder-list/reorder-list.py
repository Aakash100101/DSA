# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow.next
        slow.next=None

        prev=None
        curr=second
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        p1=head
        p2=prev
        while p2:
            next1=p1.next
            next2=p2.next

            p1.next=p2
            p2.next=next1

            p1=next1
            p2=next2
           

        
        """
        Do not return anything, modify head in-place instead.
        """
        