# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        best=root
        node=root
        while node:
            if abs(node.val-target)<abs(best.val-target):
                best=node
            node=node.left if target<node.val else node.right
        return best.val
        