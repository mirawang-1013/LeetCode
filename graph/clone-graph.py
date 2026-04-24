
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #第一句都是考虑如果是空集会怎么样
        if not node:
            return None

        old_to_new={node:Node(node.val)} #建新节点
        queue = deque([node]) #建立queue

        while queue:
            curr=queue.popleft() #把排在queue的第一个node pop出来
            for i in curr.neighbors:
                if i not in old_to_new:
                    old_to_new[i]=Node(i.val)
                    queue.append(i) #加入queue后，后续再处理它的邻居
                old_to_new[curr].neighbors.append(old_to_new[i]) #这就是把当前的curr和后续的邻居连接起来，不写的话就会分不出来node的邻居是什么。
        return old_to_new[node]

