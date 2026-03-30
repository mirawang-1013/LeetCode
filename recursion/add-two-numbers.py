# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        dummy = ListNode(0)
        new=dummy
        carry=0
        while l1 or l2 or carry:  #为什么在这里l1, l2他是listnode但是不需要额外赋值啥的
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            
            total = val1+val2+carry
            carry=total//10 

            new.next=ListNode(total%10)
            new=new.next
            if l1:
                l1=l1.next 
            if l2:
                l2=l2.next
        return dummy.next
