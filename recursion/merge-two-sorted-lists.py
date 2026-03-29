# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List 

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy

        while list1 and list2:
            if list1.val<list2.val:
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next 
        #上面选出了下一个字符后，这句话是为了完成现有node对下一个node的指向的
        curr.next= list1 if list1 else list2
        return dummy.next


            

























      #history method
        #       dummy = ListNode()
        # tail = dummy
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         tail.next = list1
        #         list1 = list1.next
                
        #     else:
        #         tail.next = list2
        #         list2 = list2.next
        #     tail = tail.next
        # if list1:
        #     tail.next = list1
        # else:
        #     tail.next = list2
        # return dummy.next
