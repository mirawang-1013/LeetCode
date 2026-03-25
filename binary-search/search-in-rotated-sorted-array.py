class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[left]: #如果左邊可能是升序
                if nums[mid]>target>=nums[left]: #若左邊是升序
                    right=mid-1
                else: #左邊不是升序了，但右邊是升序
                    left=mid+1
            else: #若右邊可能是升序
                if nums[mid]<target<=nums[right]: #若右邊是升序
                    left=mid+1
                else: #右邊不是升序了，但左邊是升序
                    right=mid-1
        return -1
            