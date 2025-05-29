import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #如果list什么也没有就返回None
        if not lists or len(lists) == 0:
            return None
        #当list有内容的时候，创建一个stack来暂时保存两两合并的新链表
        while len(lists) > 1:
            merge=[]
        #
            for i in range(0,len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                #每两个链表之间合并
                merge.append(self.mergeList(l1,l2))
            lists = merge
        return lists[0]

    def mergeList(self,l1,l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next