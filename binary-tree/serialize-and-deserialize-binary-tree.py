# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node: #若没有结点就用null填充
                vals.append("null")
                return 
            vals.append(str(node.val)) #把值都装进来
            #先序遍历（根-左-右）
            dfs(node.left) 
            dfs(node.right)
        
        vals = []
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            val = next(vals)
            if val == "null":
                return None #空结点
            node = TreeNode(int(val)) #return一个值为val的TreeNode节点
            node.left = dfs() #递归还原左子树，#递归还原右子树
            node.right = dfs()
            return node
        vals = iter(data.split(","))
        return dfs()

        #the function of iter is to
        #"1,2,null,null,3,null,null" → ["1", "2", "null", "null", "3", "null", "null"]。
        #然后用 iter() 把它变成一个迭代器 vals，这样就可以用 next() 一个个依次取出元素
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))