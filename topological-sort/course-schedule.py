from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        courses = prerequisites
        for a, b in courses:
            g[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]
            if state == VISITED: return True
            elif state == VISITING: return False

            states[node] = VISITING #start to explore

            for neighbor in g[node]:
                if not dfs(neighbor): #没找到闭环的，就标记为visited
                    return False
            
            states[node] = VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True










