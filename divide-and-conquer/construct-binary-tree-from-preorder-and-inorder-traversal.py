# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        #preorder第一个肯定是根了
        root_val = preorder[0] 
        root = TreeNode(root_val) #找到根了

        # 在中序中找到根节点的位置，找到根的index
        mid=inorder.index(root_val)

        # 划分左右子树,左子树等于根之前的部分，
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        
        return root