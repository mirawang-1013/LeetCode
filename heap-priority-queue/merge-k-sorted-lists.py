import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        count = 0  # 保证每个元素唯一

        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, count, l))
                count += 1

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, count, node.next))
                count += 1

        return dummy.next
