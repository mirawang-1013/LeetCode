class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current_num=max_num=nums[0]
        for i in nums[1:]:
            current_num=max(i,i+current_num)
            max_num=max(max_num, current_num)
        return max_num
            
  







