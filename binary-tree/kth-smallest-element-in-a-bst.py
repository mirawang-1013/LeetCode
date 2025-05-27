# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root) #给stack push 根
                root = root.left #先遍历左边的节点，把小于root的全部压入stack
            #当root = None的时候，可以pop stack
            root = stack.pop()
            k-=1
            if k==0:
                return root.val
            root=root.right
        