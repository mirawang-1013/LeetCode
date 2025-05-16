
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

        visited = {} #原node -> 复制新的node

        def dfs(curr):
            if curr in visited:      # 避免重复或死循环
                return visited[curr]

            clone = Node(curr.val)   # 先复制当前节点
            visited[curr] = clone    # 马上存进 visited

            for neighbor in curr.neighbors:   # 遍历邻居
                clone.neighbors.append(dfs(neighbor))  # 递归复制邻居

            return clone             # 返回当前复制结果

        return dfs(node)         # 最终返回整个复制图的入口节点

