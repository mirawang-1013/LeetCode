class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        p1,p2=0,0
        length=0

        while p1<len(text1) and p2<len(text2):
            if text1[p1]==text2[p2]:
                length+=1
                p1+=1
                p2+=1
            else:
                p1+=1
        return length


        