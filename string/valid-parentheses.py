class Solution:
    def isValid(self, s: str) -> bool:
        pairs={')':'(',']':'[','}':'{'}
        stack = []
        
        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack
#return not stack equals to
# if len(stack) == 0:
#     return True
# else:
#     return False


       