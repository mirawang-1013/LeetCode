class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]

        for i in strs[1:]:
            while i.startswith(prefix)!=True:
                prefix = prefix[:-1] 
        return prefix
