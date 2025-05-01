class Solution:
    def longestPalindrome(self, s: str) -> str:
        #the code doesn't explicitly check whether the entire string s is of odd or even length. Instead, it assumes every character position could be the center of a palindrome, and it handles both odd-length and even-length palindromes independently using two passes inside the same loop.
        res = ""
        resLen = 0 # the variable to record longest length

        # odd order
        for i in range(len(s)):
            l,r  = i,i #start from the same element
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        # even order
            l, r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1)>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        return res
        