# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #双指针试试
        p1,p2=len(head)-2,len(head)-1
        List=[]
        for p1,p2 in range(len(head)-1,-1,-1):
            List.append(p2)
            p2=p1


        # stack 的解法
        # stack=[]
        # if not head:
        #     return None
        # curr=head
        # while curr:
        #     stack.append(curr.val)
        #     curr=curr.next
        # new_head=ListNode(stack.pop())
        # curr=new_head
        # while stack:
        #     curr.next=ListNode(stack.pop())
        #     curr=curr.next
        # return new_head
        
        