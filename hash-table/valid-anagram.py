from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in s:
            dict1[i]=dict1.get(i,0)+1
        for j in t:
            dict2[j]=dict2.get(j,0)+1
        return dict1==dict2

    #    return Counter(s) ==  Counter(t)
   #Solution 2     
        # pair1=[]
        # pair2=[]
        # s=sorted(s)#don't put the sorted function in loop, too slow
        # t=sorted(t)
        # if len(s) != len(t):
        #     return False
        # for i in s:
        #     pair1.append(i)
        # for j in t:
        #     pair2.append(j)
        # if pair1 == pair2:
        #     return True
        # else: 
        #     return False
        