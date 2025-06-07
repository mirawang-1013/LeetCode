class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        res = []

        def backtrack(index:int, path:str):
            if index == len(digits):# 数字都梳理完成
                res.append(path)
                return
            
            #数字还没有处理完
                possible_letters = phone_map[digits[index]]
                for letter in possible_letters:
                    backtrack(index+1, path+letter)
        #initialize
        backtrack(0,"")
        return res