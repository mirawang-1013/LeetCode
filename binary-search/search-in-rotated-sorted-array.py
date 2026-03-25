class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)-1
        if target not in nums:
            return -1
        while left<right:
            mid = (left+right)//2   
            if nums[mid]>target and nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return left
            