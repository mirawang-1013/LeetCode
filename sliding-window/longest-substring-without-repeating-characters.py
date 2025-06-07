class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        l = 0
        res= 0
        for r in range(len(s)):
            while s[r] in subString:
                subString.remove(s[l])
                l+=1
            subString.add(s[r])
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















