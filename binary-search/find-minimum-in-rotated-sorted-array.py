class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                #minimum value is on the right side
                left = mid+1
                #minimum value is on the left side
            else:
                right = mid
        
        return nums[left]
        