class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)== 0:
            return False
    
        start = 0
        end = len(s)-1
        while start<end:
                    # Skip non-alphanumeric characters from the start
            while start < end and not s[start].isalnum():
                start += 1
            # Skip non-alphanumeric characters from the end
            while start < end and not s[end].isalnum():
                end -= 1
       
            if s[start].lower()!=s[end].lower():
                return False
            start+=1
            end-=1
        return True
            