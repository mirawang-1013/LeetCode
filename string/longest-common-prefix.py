class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for c in strs[1:]:
            while c.startswith(prefix)!=True:
                prefix = prefix[:-1]
        return prefix

        

