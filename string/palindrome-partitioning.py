class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #answer
        res = []
        #store path
        path = []

        #判断是否是回文
        def is_palindrome(sub):
            #正着数=倒着数
            return sub == sub[::-1]
        
        #回溯
        def backtrack(start):
            #当开始的点等于s的长度
            if start == len(s):
                #加入路径
                res.append(path[:])
                return

                #当确定了start的点，开始loop start后面的每个字符，一直到s的最后一个字符
            for end in range(start+1,len(s)+1):
                #哪一节是回文,start是固定的，end是顺着range一个一个往下推
                if is_palindrome(s[start:end]):
                    #如果是回文，就把这个字段放进去
                    path.append(s[start:end])
                    #然后以字段结束为起点，再继续找下一个回文字符串
                    backtrack(end)
                    path.pop()
        backtrack(0)
        return res
