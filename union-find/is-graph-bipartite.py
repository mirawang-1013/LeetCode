from collections import deque
#graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
#output = false/true
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1]*n  # a bipartite set that store uncolored and colored info of the node
        # -1: uncolored, 0: group A, 1: group B
    
        for i in range(n):
            if color[i] == -1:
                queue = deque() # create a queue to start traversal
                queue.append(i)
                color[i] = 0 #initialize with color 0

            while queue:
                node = queue.popleft() #pop the left one out
                for neighbor in graph[node]:
                    if color[neighbor] == -1 :
                        #this is the most tricky step to mark the color of the node
                        #once the value is 0 then the neighbor would be 1
                        #if the value is 1 then the neighbor would be 0
                        color[neighbor]=1 - color [node]
                        #after traverse the node, put the neighbor into the queue to traverse the nearby node as well
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # Found conflict, if the two adjacent node is the same, then just return false
                        return False
        return True
        