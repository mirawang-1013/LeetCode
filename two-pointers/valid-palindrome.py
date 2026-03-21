class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = [i.lower() for i in s if i.isalnum()]
        return normalized[::]==normalized[::-1]

