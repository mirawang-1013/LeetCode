class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        alphabet_dict={}
        for a in s:
            if a not in alphabet_dict:
                alphabet_dict[a]=1
            else:
                num=alphabet_dict.get(a,0)+1
                alphabet_dict[a]=num
        return max(alphabet_dict.values())