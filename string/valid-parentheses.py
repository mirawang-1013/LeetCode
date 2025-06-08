class Solution:
    def isValid(self, s: str) -> bool:
        pairs={")":"(","}":"{","]":"["}
        stack = []
        for i in s:
            if i in pairs:
                if not stack or pairs[i]!=stack[-1]:
                    return False
                stack.pop()
            else:
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