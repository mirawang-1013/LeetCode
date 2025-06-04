class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #用set()来装substring, for no repeating characters
        subString = set()
        #初始化左指针
        l=0
        #length是0
        res=0
        #若是substring已经有了同样的字符，那左边的指针可以往右移动一个
        for r in range(len(s)):
            while s[r] in subString:
                subString.remove(s[l])
                l+=1
            #不然的话可以往substring里添加字符
            subString.add(s[r])
            #把最长的距离存到res中去
            res = max(res,r-l+1)
        return res



















        # subString = set()
        # l = 0
        # res = 0
        # for r in range(len(s)):
        #     while s[r] in subString: #若出现重复的字符
        #         subString.remove(s[l])
        #         l+=1 #把左边的指针向右移动
        #     subString.add(s[r])
        #     res = max(res, r-l+1)
        # return res















