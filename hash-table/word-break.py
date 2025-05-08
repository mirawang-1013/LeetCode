class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        def dp(s: str) -> bool:
            if s in words: return True
            for i in range(min(len(s),20)):
                if s[:i] in words and dp(s[i:]): 
                    return True
            return False
        
        return dp(s)
        