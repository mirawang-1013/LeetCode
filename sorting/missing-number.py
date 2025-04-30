class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums)+1):
            if i not in num_set:
                return i
        # math method
        # n = len(nums)
        # total = n*(n+1)//2
        # actual = sum(nums)
        # missing = total-actual

        # return missing
        
