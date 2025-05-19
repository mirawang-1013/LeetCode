class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #build adjacency list
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        components = 0

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1
        
        return components
