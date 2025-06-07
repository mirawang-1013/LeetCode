from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #thinking process: 若t为空，则返回空；have和need,遍历右指针，当左指针收缩时，have和need相等就存下最短的长度，遍历完右指针之后返回最短的长度
        if t =="":
            return ""
        
        countT, window = {},{}  
        for c in t:
            #将目标查找的函数计数
            # .get(c, 0) 的意思是“如果没见过这个字符，就当它是 0 次"
            countT[c] = 1+countT.get(c,0)

        #初始化have和need
        #初始化结果指针的位置和结果的长度
        have,need = 0,len(countT)
        res,resLen = [-1,-1],float("infinity")
        l=0

        #右指针滑动窗口
        for r in range(len(s)):
            c = s[r]
            #找这个have窗口里能有多少字符和对应的计数
            window[c] = 1+window.get(c,0)

            #如果c在这个need中，且need和have相等
            if c in countT and window[c] == countT[c]:
                have+=1
            
            while have == need:
                #如果更短，那就缩短have
                if(r-l+1)<resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]] -= 1
                #左边缩短到使得have小于need了
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                #左边的指针向右移动
                l+=1
        l,r = res
        return s[l:r+1] if resLen!=float("infinity") else ""
            
