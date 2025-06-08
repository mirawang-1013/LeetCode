class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        tele = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
}

        res = []

        def backtrack(index,path):
            if index ==len(digits):
                res.append(path)
                return 
            
            for i in tele[digits[index]]:
                backtrack(index+1,path+i)
        
        backtrack(0,"")
        return res