# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        if not head:
            return None
        curr=head
        while curr:
            stack.append(curr.val)
            curr=curr.next
        new_head=ListNode(stack.pop())
        curr=new_head
        while stack:
            curr.next=ListNode(stack.pop())
            curr=curr.next
        return new_head
        
        