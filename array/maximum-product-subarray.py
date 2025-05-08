class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, len(nums)):
            n=nums[i]
            if n<0:
                cur_max,cur_min = cur_min,cur_max
            cur_max=max(n,n*cur_max)
            cur_min=max(n,n*cur_min)

            max_prod = max(max_prod, cur_max)
        
        return max_prod

        