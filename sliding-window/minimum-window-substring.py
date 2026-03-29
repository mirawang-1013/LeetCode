from collections import Counter
# 先统计 t 里每个字符需要多少个
# missing 表示总共还缺多少个字符
# right 不断往右扩张窗口
# 每加入一个字符，就更新 need 和 missing
# 一旦 missing == 0，说明当前窗口已经包含了 t 的所有字符
# 这时尝试不断移动 left，看看能不能把窗口缩得更短
# 缩的时候，如果移走的是“关键字符”，导致重新缺字符了，就停止缩小
# 过程中不断更新最短答案
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #1.先计数，找到记录需要的字符和缺失的字符的办法
        #2.然后开始遍历s,等到窗口长到可以满足找到所有缺失字符时，再尝试着从左边开始缩小窗口
        #3.直到不能缩小的时候就返回字符串

        need = Counter(t)
        missing = len(t)
        min_len=float('inf')
        left=0
        start=0
        for right in range(len(s)):
            if need[s[right]]>0:
                missing-=1
            need[s[right]]-=1
        
        while missing==0:
            if right-left+1<min_len:
                min_len=right-left+1
                start=left
            need[s[left]]+=1
            if need[s[left]]>0:
                missing+=1
            left+=1
        return "" if min_len==float('inf') else s[start:start+min_len]





















        # need=Counter(t)
        # missing=len(t)
        # left=0
        # min_len = float('inf')
        # for right in range(len(s)):
        #     if need[s[right]]>0:
        #         missing-=1
        #     need[s[right]]-=1

        #     while missing==0:
        #         if right-left+1<min_len:
        #             start=left #为什么这步要这么定义呢
        #             min_len=right-left+1
        #         need[s[left]] += 1 
        #         if need[s[left]]>0:
        #             missing+=1 #破坏平衡，左边不能再缩小窗口了
        #         left +=1
        # return "" if min_len == float('inf') else s[start:start + min_len]







        # if not t:
        #     return ""

        # countT, window = {},{}

        # for c in t:
        #     countT[c] = 1+countT.get(c,0) #t="AABC" → {'A':2, 'B':1, 'C':1}）
        
        # have,need = 0,len(countT)# have: 当前窗口已满足的字符数；need: 总共需要满足的字符数

        # res,resLen = [-1,-1],float("infinity") # 记录最短子串的左右边界和长度
        # l=0 # 窗口左指针

        # for r in range(len(s)):  # r: 窗口右指针
        #     c = s[r]
        #     window[c] = 1+window.get(c,0)  # 将当前字符加入窗口计数
        
        #     if c in countT and window[c] == countT[c]:
        #         have+=1

        #     while have == need:
        #         #收缩窗口
        #         if(r-l+1)<resLen:
        #             res = [l,r]
        #             resLen = r-l+1
        #         window[s[l]]-=1
        #         #减少窗口里的have计数
        #         if s[l] in countT and window[s[l]]<countT[s[l]]:
        #             have-=1
        #         l+=1
        # l,r = res
        # return s[l:r+1] if resLen!=float("infinity")else""


        # #thinking process: 若t为空，则返回空；have和need,遍历右指针，当左指针收缩时，have和need相等就存下最短的长度，遍历完右指针之后返回最短的长度
        # if t =="":
        #     return ""
        
        # countT, window = {},{}  
        # for c in t:
        #     #将目标查找的函数计数
        #     # .get(c, 0) 的意思是“如果没见过这个字符，就当它是 0 次"
        #     countT[c] = 1+countT.get(c,0)

        # #初始化have和need
        # #初始化结果指针的位置和结果的长度
        # have,need = 0,len(countT)
        # res,resLen = [-1,-1],float("infinity")
        # l=0

        # #右指针滑动窗口
        # for r in range(len(s)):
        #     c = s[r]
        #     #找这个have窗口里能有多少字符和对应的计数
        #     window[c] = 1+window.get(c,0)

        #     #如果c在这个need中，且need和have相等
        #     if c in countT and window[c] == countT[c]:
        #         have+=1
            
        #     while have == need:
        #         #如果更短，那就缩短have
        #         if(r-l+1)<resLen:
        #             res = [l,r]
        #             resLen = r-l+1
        #         window[s[l]] -= 1
        #         #左边缩短到使得have小于need了
        #         if s[l] in countT and window[s[l]] < countT[s[l]]:
        #             have -= 1
        #         #左边的指针向右移动
        #         l+=1
        # l,r = res
        # return s[l:r+1] if resLen!=float("infinity") else ""
            
