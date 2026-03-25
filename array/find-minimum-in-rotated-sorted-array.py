class Solution:
    def findMin(self, nums: List[int]) -> int:
        rotate_times = nums[0]
        if len(nums)%2!=0:
            rotate_times= rotate_times % len(nums)
        else:
            rotate_times= (rotate_times+1) % len(nums)
        return nums[rotate_times]



        
        