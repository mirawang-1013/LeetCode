from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet=set()
        def dfs(crs):
            if crs in visitSet:
                return False #有闭环了，不成立
            
            if preMap[crs]==[]:
                return True #如果不依赖任何课程，那就成功
            
            visitSet.add(crs) #在访问过的集合里加上课程
            for pre in preMap[crs]: 
                if not dfs(pre): #只要有一门前置课完不成，就不行
                    return False #对于课程的前置课程，如果闭环了，那就返回false
            visitSet.remove(crs) #如果能跑的通，就把这个course移除掉
            preMap[crs]=[] #把这门course的依赖项清空
            return True
        for crs in range(numCourses):
            if not dfs(crs): #只要有一门课程出现闭环就不行
                return False  
        return True







        # preMap = {i:[] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)
        
        # visitSet = set()
        # def dfs(crs):
        #     if crs in visitSet:
        #         return False
            
        #     if preMap[crs]==[]:
        #         return True
            
        #     visitSet.add(crs)
        #     for pre in preMap[crs]:
        #         if not dfs(pre):
        #             return False
                
        #     visitSet.remove(crs)
        #     preMap[crs]=[]
        #     return True
        # for crs in range(numCourses):
        #     if not dfs(crs): return False
        # return True
