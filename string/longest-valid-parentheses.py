class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        max_valid=0

        for index,value in enumerate(s):
            if value == '(':
                stack.append(index)
            else:
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    max_valid=max(max_valid,index-stack[-1])
        return max_valid


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