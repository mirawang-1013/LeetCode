# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #如果没有根，就返回空
        if not root:
            return []
        
        #先创建result,之后是用来存放一层一层的node的
        result = []
        queue = deque([root]) #用队列来保存当前层的节点

        #当前层的节点数是用来遍历左子节点和右子节点的
        while queue:
            level_size = len(queue) #当前层节点数
            level = []  #当前层的结果列表

            #把level里的节点pop出来，加入到level中去
            #如果左右节点，也继续append
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
            #queue是用来收集下一层的node的
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
        return result
