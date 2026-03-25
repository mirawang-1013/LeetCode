class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)-1
        if target not in nums:
            return -1
        
        while left<=right: # use <= instead of < 
            mid = (left+right)//2   
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]: # left half is sorted
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            
            else:  # right half is sorted
                if nums[mid]<target<=nums[right]:  # use <= for right boundary
                    left=mid+1
                else: 
                    right=mid-1
        return -1