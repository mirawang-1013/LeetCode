class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #初始stack
        stack = [-1]
        #最长长度
        max_len=0

        #遍历s,带着index和character来遍历的
        for i,char in enumerate(s):
            if char=='(':
                stack.append(i)
            else:#如果是)
                stack.pop()
                if not stack:
                    stack.append(i)#记录当前不匹配的位置，为什么呢
                else:
                    max_len = max(max_len,i-stack[-1])
        return max_len

"""
s = "()(()"
indexes: 0 1 2 3 4

遍历过程：
- i=0: s[0] = '(' → push(0) => stack = [-1, 0]
- i=1: s[1] = ')' → pop() => stack = [-1] → 有效 → i - stack[-1] = 1 - (-1) = 2 ✅
- i=2: s[2] = '(' → push(2) => stack = [-1, 2]
- i=3: s[3] = '(' → push(3) => stack = [-1, 2, 3]
- i=4: s[4] = ')' → pop() => stack = [-1, 2] → 有效 → i - stack[-1] = 4 - 2 = 2

所以 max_len = max(2, 2) = 2
"""