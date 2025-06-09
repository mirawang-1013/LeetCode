class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            #i是下标，jump是数值
            #i+jump是最大的能覆盖的index
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+jump)
            
        return True
