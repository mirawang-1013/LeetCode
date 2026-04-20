class Solution:
    def isPalindrome(self, s: str) -> bool:
        nomalized = [i.lower() for i in s if i.isalnum()]
        return nomalized[::]==nomalized[::-1]




        # normalized = [i.lower() for i in s if i.isalnum()]
        # return normalized[::]==normalized[::-1]

