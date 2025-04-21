class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pair = {}
        for i,n in enumerate(nums):
            if n in pair:
                return True
            pair[n] = i
        return False
        