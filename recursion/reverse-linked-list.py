# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr=curr.next
        if not stack:
            return None
        
        new_head = stack.pop()
        curr = new_head
        while stack:
            curr.next = stack.pop()
            curr = curr.next
            
        curr.next = None
        return new_head
            
       
    
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        #创建一个栈来存储数据
        stack = []
        #当前的节点是头
        curr = head
        #给栈里加节点
        while curr:
            stack.append(curr)
            #让当前箭头指向下一个节点
            curr = curr.next
        
        if not stack:
            return None
        
        #新的list是从stack的最后一个pop出来
        new_head = stack.pop()
        #现在节点 = 最后一个pop出来的
        curr = new_head
        #当stack里还有数的时候，下一个node等于stack里的下一个数
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        
        curr.next = None
        return new_head
        