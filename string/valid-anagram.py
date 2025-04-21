class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pair1=[]
        pair2=[]
        s=sorted(s)
        t=sorted(t)
        if len(s) != len(t):
            return False
        for i in s:
            pair1.append(i)
        for j in t:
            pair2.append(j)
        if pair1 == pair2:
            return True
        else: 
            return False
        