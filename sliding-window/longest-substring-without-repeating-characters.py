class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        LongLeg=0
        sub=deque()
        for i in s:
            while i in sub:
                sub.popleft()
            sub.append(i)
            LongLeg=max(len(sub),LongLeg)
        return LongLeg


        # #当有not repeating 需求的时候都是set()
        # substring = set()
        # l=0
        # L=0
        # for r in range(len(s)):
        #     while s[r] in substring:
        #         substring.remove(s[l])
        #         #remove是按照什么顺序在remove?
        #         l+=1
        #     substring.add(s[r])          
        #     L=max(L,r-l+1)
        #     #取最长的时候一般都会用到这个max()的函数
        # return L
















