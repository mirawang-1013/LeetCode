class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left<=right:
            #确定中点的位置
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            #如果左边是升序，就用二分法找
            if nums[left] <= nums[mid]:
                if nums[left] <= target <nums[mid]:
                    right = mid -1
                else:
                    left = mid+1
            #如果右边是升序同样的方法找
            else:
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1