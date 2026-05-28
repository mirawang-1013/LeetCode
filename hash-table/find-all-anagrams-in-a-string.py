from collections import Counter
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_ana=len(p)
        answer=[]
        for i,v in enumerate(s):
            if i<=len(s)-len_ana:
                new_sub=s[i:i+len_ana]
                a=sorted(Counter(new_sub))
                b=sorted(Counter(p))
                if a==b:
                    answer.append(i)
        return answer






















        # res = []
        # if len(p)>len(s):
        #     return res

        # p_count = Counter(p) #字符串substring的频率
        # s_count = Counter(s[:len(p)])#初始窗口的字母频率

        # if s_count == p_count:
        #     res.append(0) #起点的第一个index就是
        # #for i in range(3,10)
        # for i in range(len(p),len(s)):
        # #start_char = s[0]/[1]/[2]/[3]
        #     start_char = s[i-len(p)]
        #     end_char = s[i]

        #     # 移出窗口最左边的字符
        #     s_count[start_char] -= 1
        #     #删除为0的键，以免被误判
        #     if s_count[start_char] == 0:
        #         del s_count[start_char] 

        #     s_count[end_char] += 1

        #     if s_count == p_count:
        #         res.append(i - len(p) + 1)

        # return res
        