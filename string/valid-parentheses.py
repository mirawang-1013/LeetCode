class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}":"{","]":"[",")":"("}
        stack = []
        for i in s: #遍历s里的括号
            if i in pairs: #如果是右括号
                if not stack or pairs[i]!=stack[-1]: #看stack是否为空，或者是否有左括号可以匹配
                    return False
                else:
                    stack.pop()
            else: #如果是左括号
                stack.append(i) 
        return not stack


















        # pairs = {')': '(', ']': '[', '}': '{'}
        # stack = []
        # for c in s:
        #     if c in pairs:
        #         if not stack or stack[-1]!=pairs[c]:
        #             return False
        #         stack.pop()
        #     else:
        #         stack.append(c)
        # return not stack