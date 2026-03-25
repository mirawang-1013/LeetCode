class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)-1
        if target not in nums:
            return -1
        mid=(len(nums)-1)//2
        while left<=right:
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid
                mid=(right+left)//2
            else:
                right=mid
                mid=(right+left)//2
        return -1

