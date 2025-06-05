class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]


    #Solution
        # l,r = 0, len(s)-1

        # while l<r:
        #     if not self.isAlNum(s[l]):
        #         l+=1
        #         continue
               
        #     if not self.isAlNum(s[r]):
        #         r-=1
        #         continue
         
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l,r = l+1, r-1
        # return True


    def isAlNum(self,c):
        return ((ord('A')<= ord(c)<= ord('Z')) or 
        (ord('0')<=ord(c)<=ord('9')) or 
        (ord('a')<=ord(c)<=ord('z'))
        )