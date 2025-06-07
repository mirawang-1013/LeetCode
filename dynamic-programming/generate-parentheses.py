class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path:str, open_count:int, close_count:int):
            #结束的条件是左括号和右括号都用完了
            if open_count == n and close_count == n:
                res.append(path)
                return 
            
            if open_count<n:
                backtrack(path+'(',open_count+1,close_count)
             # 右括号必须比左括号少才能放
            if close_count<open_count:
                backtrack(path+')',open_count,close_count+1)

        backtrack("",0,0)        
        return res