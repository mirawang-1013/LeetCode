# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 当前节点的最大深度 = 左右子树最大深度中的较大值 + 当前节点本身
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxLeft=self.maxDepth(root.left)
        maxRight=self.maxDepth(root.right)
        return max(maxLeft,maxRight)+1














        # if not root:
        #     return 0
        # maxLeft=self.maxDepth(root.left)
        # maxRight=self.maxDepth(root.right)
        # return max(maxLeft,maxRight)+1