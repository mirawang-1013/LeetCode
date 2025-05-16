# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#这种题真是太绝了
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)  # 建一个 dummy node 方便处理头节点被删的情况
        slow=fast=dummy

        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            fast=fast.next
            slow=slow.next
        
        slow.next = slow.next.next

        return dummy.next
