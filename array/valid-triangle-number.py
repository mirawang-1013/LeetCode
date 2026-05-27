class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count=0
        nums.sort()
        
        for i in nums[len(nums):1:-1]:
            l=0
            r=i-1
            if nums[l]+nums[r]>i:
                count+=r-l-1
                r-=1
                
            else:
                l+=1
        return count
            
        