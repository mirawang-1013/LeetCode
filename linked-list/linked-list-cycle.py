# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr=head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr=curr.next
        return False














        # visited=set()
        # curr=head
        # while curr:
        #     if curr in visited:
        #         return True
        #     else:
        #         visited.add(curr)
        #         curr=curr.next
        # return False

#为什么必须是set()?