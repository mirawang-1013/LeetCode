# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 

        #1.找重点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next #每次移动1个点
            fast = fast.next.next #每次移动2个点
        
        #2.反转后半段链表
        prev, curr = None, slow.next
        slow.next = None 
        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
        
        #merge the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2