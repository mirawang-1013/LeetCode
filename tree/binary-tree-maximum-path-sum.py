# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res= float("-inf")
        def dfs(root):
            if not root:
                return 0
            
            left=max(dfs(root.left),0)
            right=max(dfs(root.right),0)

            self.res = max(self.res, root.val+left+right)

            return root.val+max(left,right)
        dfs(root)
        return self.res









        # self.res = float("-inf") #全局变量
        # def dfs(root): #返回当前节点可以拿到的最大收益
        #     if not root:
        #         return 0 #如果已经空了，那就没有节点可以返回了

        #     left = max(dfs(root.left),0) #如果收益小于零，可以不要
        #     right = max(dfs(root.right),0) #同理

        #     self.res = max(self.res,root.val+left+right)

        #     return root.val+max(left,right) #返回当前节点和左边或者右边的最大值
        
        # dfs(root)
        # return self.res
