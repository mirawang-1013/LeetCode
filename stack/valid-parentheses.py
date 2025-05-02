class Solution:
    def isValid(self, s: str) -> bool:
        pairs={')':'(',']':'[','}':'{'}
        stack = []
        array=()
        
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char in ')]}':
                if not stack or stack.pop() != pairs[char]:
                    return False      
        return not stack
#return not stack equals to
# if len(stack) == 0:
#     return True
# else:
#     return False


       