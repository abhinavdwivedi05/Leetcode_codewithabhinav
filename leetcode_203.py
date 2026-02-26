# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        temp=ListNode(0)

        temp.next=head

        n=temp

        while n.next:

            if n.next.val==val:

                n.next=n.next.next
            else:
                n=n.next

        return temp.next

